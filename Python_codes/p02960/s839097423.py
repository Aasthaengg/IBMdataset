S = input()[::-1]
keta = len(S)
mod = 10 ** 9 + 7

dp = [[0 for _ in range(13)] for _ in range(keta + 1)]
dp[0][0] = 1
tmp = 1
for i in range(1, keta + 1):
    if S[i - 1] != "?":
        x = int(S[i - 1]) * (tmp) % 13
        for j in range(13):
            dp[i][(x + j) % 13] += dp[i - 1][j] % mod
    else:
        for k in range(10):
            x = k * (tmp) % 13
            for j in range(13):
                dp[i][(x + j) % 13] += dp[i - 1][j] % mod
    tmp *= 10
    tmp %= 13

print(dp[keta][5] % mod)
