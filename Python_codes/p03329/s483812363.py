import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
INF = 10**9

if __name__ == "__main__":
    n = int(input())
    m = [1]
    dp = [101010]*201010
    t = 6
    q = 9
    while t<=n:
        m.append(t)
        t*=6
    while q<=n:
        m.append(q)
        q*=9
    for i in m:
        dp[i] = 1
    
    for i in range(1,n):
        for j in m:
            dp[i+j] = min(dp[i+j],dp[i]+1)
    print(dp[n])