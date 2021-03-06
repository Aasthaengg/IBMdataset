import math
import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,s = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]
    mod = 998244353
    two = [1]*(n+1)
    for i in range(n):
        two[i+1] = two[i]*2%mod
    dp = np.zeros(3010,dtype = int)
    dp[0] = 1
    for i,ai in enumerate(a):
        ndp = dp*2
        ndp[ai:] += dp[:-ai]
        ndp %= mod
        dp = ndp
    print(dp[s])
    return

if __name__ == '__main__':
    main()
