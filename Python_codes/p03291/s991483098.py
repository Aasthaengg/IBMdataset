# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# DP[0, 0], Aの数、ABの数、ABCの数
MOD = 10 ** 9 + 7
S = sr()
dp = [0, 0, 0]
total = 1
for s in S:
    if s == 'A':
        dp[0] += total
    elif s == 'B':
        dp[1] += dp[0]
    elif s == 'C':
        dp[2] += dp[1]
    elif s == '?':
        dp[2] = dp[2]*3 + dp[1]
        dp[1] = dp[1]*3 + dp[0]
        dp[0] = dp[0]*3 + total
        total *= 3
    total %= MOD; dp[0] %= MOD; dp[1] %= MOD; dp[2] %= MOD
    #print(dp, total)

answer = dp[2] % MOD
print(answer)
