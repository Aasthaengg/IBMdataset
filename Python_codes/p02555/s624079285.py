import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
INF = 10**9


if __name__ == "__main__":
    s = int(input())
    MOD = 10**9 + 7
    dp = [0]*(s + 1)
    if s>=3:
        dp[3] = 1
    for i in range(4,s+1):
        dp[i] = (dp[i-3] + dp[i-1])%MOD
    print(dp[s])