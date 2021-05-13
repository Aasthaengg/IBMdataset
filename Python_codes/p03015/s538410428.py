L = input()

MOD = 10**9 + 7

# i: 決定した桁数
# j: a+b < L[i]を満たすか
dp = [[0] * 2 for _ in range(len(L) + 1)]

dp[0][0] = 1

for i in range(len(L)):
    for j in range(2):
        # (a,b) = (0,0)
        if int(L[i]):
            dp[i+1][1] += dp[i][j]
            dp[i+1][1] %= MOD
        else:
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD

        # (a,b) = (0,1), (1,0)
        if int(L[i]) or j:
            dp[i+1][j] += dp[i][j] * 2
            dp[i+1][j] %= MOD

print((dp[-1][0] + dp[-1][1]) % MOD)