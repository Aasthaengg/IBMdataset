MOD = 10 ** 9 + 7

s = input()
l = len(s)
dp = [[0 for _ in range(13)] for _ in range(l + 1)]
dp[0][0] = 1
for i in range(l):
    if s[i] == "?":
        for k in range(10):
            for j in range(13):
                pos = (j * 10) + k
                pos %= 13
                dp[i + 1][pos] += dp[i][j]
                dp[i + 1][pos] %= MOD
    else:
        for j in range(13):
            pos = (j * 10) + int(s[i])
            pos %= 13
            dp[i + 1][pos] = dp[i][j]
print(dp[-1][5])