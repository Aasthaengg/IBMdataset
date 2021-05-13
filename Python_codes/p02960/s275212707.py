import sys
input = sys.stdin.readline
mod = 10**9 + 7

s = input().rstrip()
n = len(s)
s = s[::-1]

dp = [[0]*13 for _ in range(n + 1)] # dp[i][j] : i桁目まで見て13で割ってj余る個数
dp[0][0] = 1
mul = 1
for i in range(n):
    if i > 0:
        mul *= 10
        mul %= 13
    if s[i] != '?':
        s_ = int(s[i]) * mul
        for j in range(13):
            dp[i + 1][(j + s_) % 13] += dp[i][j]
            dp[i + 1][(j + s_) % 13] %= mod
    else:
        for j in range(13):
            for k in range(10):
                k *= mul
                dp[i + 1][(j + k) % 13] += dp[i][j]
                dp[i + 1][(j + k) % 13] %= mod
print(dp[-1][5])

