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
    cp = [-1 for i in range(2*10**5+1)]
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] += dp[i-1]
        c = int(ipt())
        pc = cp[c]
        if pc != -1 and pc != i-1:
            dp[i] += dp[pc]
        cp[c] = i
        dp[i] %= mod

    print(dp[-1])


    return None

if __name__ == '__main__':
    main()
