MOD = 10**9 + 7

s = input()
n = len(s)

dp = [[0]* 13 for i in range(n+1)]
dp[0][0] = 1

for i in range(n):
    if s[i] != '?':
        for j in range(13):
            a = s[i]
            a = int(a)
            keta = (j*10 + a) % 13
            dp[i+1][keta] += dp[i][j]
            dp[i+1][keta] %= MOD
    else:
        for j in range(13):
            for k in range(10):
                keta = (j*10 + k) % 13
                dp[i+1][keta] += dp[i][j]
                dp[i+1][keta] %= MOD
                
print(dp[n][5] % MOD)