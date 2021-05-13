from itertools import*
from math import*
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = float("inf")
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)

N,M = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
dp = [[0]*(M+1) for i in range(N+1)]

for n in range(N):
    for m in range(M):
        if S[n] == T[m]:
            dp[n+1][m+1] = (dp[n+1][m]+dp[n][m+1]+1)%mod
        else:
            dp[n+1][m+1] = dp[n+1][m]+dp[n][m+1]-dp[n][m]

print((dp[N][M]+1)%mod)