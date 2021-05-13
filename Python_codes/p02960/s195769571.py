S = input()[:: -1]
mod = 10 ** 9 + 7
dp = [[0 for _ in range(13)] for _ in range(len(S) + 1)]

if S[0] == "?":
    for k in range(10):
        dp[1][k % 13] += 1
else:
    dp[1][int(S[0]) % 13] += 1

tmp = 1
for i in range(2, len(S) + 1):
    tmp *= 10
    tmp %= 13
    for j in range(13):
        if dp[i - 1][j] > 0:
            if S[i - 1] == "?":
                for k in range(10):
                    dp[i][(tmp * k + j) % 13] += dp[i - 1][j] % mod
            else:
                dp[i][(tmp * int(S[i - 1]) + j) % 13] += dp[i - 1][j] % mod

print(dp[len(S)][5] % mod)