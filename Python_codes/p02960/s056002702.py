s = input()
mod = 10**9 + 7
n = len(s)
dp = [[0] * 13 for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    if s[i] != "?":
        for j in range(13):
            dp[i+1][(10 * j + int(s[i])) % 13] += dp[i][j]

    else:
        for j in range(13):
            for k in range(10):
                dp[i+1][(10 * j+k) % 13] += dp[i][j]
                dp[i+1][(10 * j+k) % 13] %= mod


print(dp[n][5])