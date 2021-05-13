s = input()[::-1]
mod = 13
p = 10 ** 9 + 7
dp = [[0] * 13 for _ in range(len(s) + 1)]
dp[0][0] = 1

for i in range(len(s)):
    if s[i] == "?":
        for j in range(10):
            d = j * pow(10, i, mod)
            for k in range(13):
                dp[i + 1][(k + d) % mod] += dp[i][k]
                dp[i + 1][(k + d) % mod] %= p
    else:
        d = int(s[i]) * pow(10, i, mod)
        for k in range(13):
            dp[i + 1][(k + d) % mod] += dp[i][k]
print(dp[-1][5])
