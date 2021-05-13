'''
研究室PCでの解答
'''
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
mod = 10**9+7 #998244353
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    n = int(ipt())
    dp = [1]*(4**3)
    dp[0*16+2*4+1] = 0
    dp[2*16+0*4+1] = 0
    dp[0*16+1*4+2] = 0
    for _ in range(n-3):
        ndp = [0]*(4**3)
        for i in range(4):
            ndp[0*16+2*4+1] -= dp[i*16+0*4+2]
            ndp[i*16+2*4+1] -= dp[0*16+i*4+2]
            ndp[2*16+i*4+1] -= dp[0*16+2*4+i]
        ndp[0*16+2*4+1] += dp[0*16+0*4+2]
        ndp[2*16+2*4+1] += dp[0*16+2*4+2]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        ndp[i*16+j*4+k] += dp[l*16+i*4+j]
        # ndp[0*16+2*4+1] = 0
        ndp[2*16+0*4+1] = 0
        ndp[0*16+1*4+2] = 0
        for i in range(4**3):
            ndp[i] %= mod
        dp = ndp*1
#        print(dp)

    ans = 0
    for i in dp:
        ans += i
    print(ans%mod)
    return None

if __name__ == '__main__':
    main()
