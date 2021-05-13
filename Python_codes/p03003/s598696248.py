# -*- coding: utf-8 -*-
# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

MOD = 10**9+7
N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

# Sのi文字目までと、Tのj文字目までで、dp[i][j]こ
dp = [[0]*(M+1) for _ in range(N+1)]

for r in range(1, N+1):
    for k in range(1, M+1):
        if S[r-1] == T[k-1]:
            dp[r][k] = 1+dp[r-1][k]+dp[r][k-1]
            dp[r][k] %= MOD
        else:
            dp[r][k] = dp[r-1][k]+dp[r][k-1]-dp[r-1][k-1]
            dp[r][k] %= MOD
print((dp[-1][-1]+1) % MOD)
