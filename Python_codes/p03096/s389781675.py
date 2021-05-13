#!/usr/bin/env python3
MOD = 10**9 + 7
N = int(input())
C = [int(input()) for _ in range(N)]

dic = dict()
dp = [None] * N
for i, x in enumerate(C):
    if x in dic:
        dp[i] = dic[x]
    dic[x] = i

dp2 = [0] * N
dp2[0] = 1
for i in range(1, N):
    dp2[i] = dp2[i - 1]
    if dp[i] is not None and i - 1 != dp[i]:
        dp2[i] = (dp2[i] + dp2[dp[i]]) % MOD

print(dp2[-1])
