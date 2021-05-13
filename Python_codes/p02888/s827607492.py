import math
#import numpy as np
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n = int(ipt())
    l = [int(i) for i in ipt().split()]
    l.sort()
    ans = 0
    dp = [[0]*(2*10**3+1) for i in range(2)]
    for i in l:
        ans += sum(dp[1][i+1::])
        for j in range(i,2*10**3+1):
            dp[1][j] += dp[0][j-i]
        dp[0][i] += 1
    print(ans)

    return None

if __name__ == '__main__':
    main()
