# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 桁DP, Lを超えないものと保留のもの
MOD = 10 ** 9 + 7
L = sr()
dp = [1, 2]
length = len(L)
for i in range(1, length):
    prev = dp[:]
    if L[i] == '1':
        dp[0] = prev[0] * 3 + prev[1]
        dp[1] = prev[1] * 2
    else:
        dp[0] = prev[0] * 3
        dp[1] = prev[1]
    dp[0] %= MOD
    dp[1] %= MOD

answer = sum(dp)
print(answer%MOD)
