mod = 10 ** 9 + 7
s = input()
n = len(s)
dp = [[0] * 13 for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    if s[i] == '?':
        for j in range(13):
            for k in range(10):
                jj = (10 * j + k) % 13
                dp[i + 1][jj] = (dp[i + 1][jj] + dp[i][j]) % mod
    else:
        k = int(s[i])
        for j in range(13):
            jj = (10 * j + k) % 13
            dp[i + 1][jj] = (dp[i + 1][jj] + dp[i][j]) % mod
print(dp[n][5])