s = input()
n = len(s)
# dp[i][j]:上からi桁目で13で割った余りがjの場合の数
dp = [[0]*13 for i in range(n+1)]
dp[0][0] = 1
mod = 10**9+7
for i in range(n):
    for j in range(13):
        if s[i] == "?":
            for k in range(10):
                dp[i+1][(j*10+k)%13] += dp[i][j]
                dp[i+1][(j*10+k)%13] %= mod
        else:
            k = int(s[i])-0
            dp[i+1][(j*10+k)%13] += dp[i][j]
            dp[i+1][(j*10+k)%13] %= mod

print(dp[n][5])