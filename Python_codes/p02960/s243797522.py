S = input()
l = len(S)
dp = [[0] * 13 for _ in range(l+1)]
dp[0][0] = 1
MOD = 10 ** 9 + 7
mul = 1
for i in range(l):
    if S[-(i+1)] == '?':
        for j in range(10):
            for k in range(13):
                dp[i+1][(j * mul + k) % 13] += dp[i][k]
                dp[i+1][(j * mul + k) % 13] %= MOD
    else:
        j = int(S[-(i+1)])
        for k in range(13):
            dp[i+1][(j * mul + k) % 13] += dp[i][k]
            dp[i+1][(j * mul + k) % 13] %= MOD
    mul = mul * 10 % 13
print(dp[l][5])