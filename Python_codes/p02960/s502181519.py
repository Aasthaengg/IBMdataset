import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    s = input()
    n = len(s)
    m13 = [0,10,7,4,1,11,8,5,2,12,9,6,3]
    dp = [0]*13
    mod = 10**9+7
    dp[0] = 1
    for i in s:
        dpp = dp*1
        if i == "?":
            dp = [0]*13
            for j in range(13):
                for k in range(10):
                    nj = m13[j]+k
                    dp[(m13[j]+k)%13] = (dp[(m13[j]+k)%13]+dpp[j])%mod
        else:
            ii = int(i)
            for j in range(13):
                dp[(m13[j]+ii)%13] = dpp[j]
    print(dp[5])
    return

if __name__ == '__main__':
    main()
