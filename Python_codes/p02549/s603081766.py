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
# mod = 10**9+7
mod = 998244353
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"
INF = 1<<32-1
# INF = 10**18

def main():
    n,k = map(int,ipt().split())
    dp = [0]*(n+1)
    dp[1] = 1
    rng = [tuple(map(int,ipt().split())) for i in range(k)]
    for i in range(2,n+1):
        for l,r in rng:
            dp[i] += dp[max(0,i-l)]-dp[max(0,i-r-1)]
        dp[i] += dp[i-1]
        dp[i] %= mod

    print((dp[n]-dp[n-1])%mod)

    return None

if __name__ == '__main__':
    main()
