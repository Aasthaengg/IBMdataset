'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n,m = map(int,ipt().split())
    s = [int(i) for i in ipt().split()]
    t = [int(i) for i in ipt().split()]
    ans = 0

    dp = [[1]*(m+1) for i in range(n+1)]
    for i,si in enumerate(s):
        for j,tj in enumerate(t):
            if si == tj:
                dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]

            else:
                dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]-dp[i][j]
            dp[i+1][j+1] %= mod

    print(dp[n][m])

    return None

if __name__ == '__main__':
    main()
