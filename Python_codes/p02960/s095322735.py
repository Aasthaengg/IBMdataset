S = input()

dp = [[0] * 13 for _ in range(len(S) + 1)]
dp[0][0] = 1
mod = 10 ** 9 + 7
for i in range(len(S)):
    for j in range(13):
        if S[i] == "?":
            for k in range(10):
                x = (j * 10 + k) % 13
                dp[i + 1][x] += dp[i][j]
                dp[i + 1][x] %= mod
        else:
            x = (j * 10 + int(S[i])) % 13
            dp[i + 1][x] += dp[i][j]
            dp[i + 1][x] %= mod
            
print(dp[-1][5])
