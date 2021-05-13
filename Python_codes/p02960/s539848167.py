s = input()
n = len(s)
MOD = 10**9 + 7
dp = [[0]*13 for _ in range(n+1)]
# dp[i][j]は先頭からi文字目を見た時の13でわったあまりがjのものの数

dp[0][0] = 1
#print(dp[0])
for i in range(n):
    if s[i] != "?":
        for j in range(13):
            dp[i+1][(10*j+int(s[i])) % 13] = dp[i+1][(10*j+int(s[i])) % 13] + dp[i][j] % MOD
    else:
        for k in range(10):
            for j in range(13):
                dp[i+1][(10*j+k) % 13] = dp[i+1][(10*j+k) % 13] + dp[i][j] % MOD
print(dp[n][5]%MOD)
