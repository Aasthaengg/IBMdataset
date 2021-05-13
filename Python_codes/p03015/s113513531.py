MOD = 10**9+7
l = input()
n = len(l)
dp = [[[0] * 2 for _ in range(3)] for _ in range(n+1)]
dp[0][0][1] = 1

for i in range(n):
    for j in range(3):
        dp[i][j][0] %= MOD
        dp[i][j][1] %= MOD
        dp[i+1][0][0] += dp[i][j][0]
        dp[i+1][1][0] += dp[i][j][0]
        dp[i+1][2][0] += dp[i][j][0]
        if l[i] == "1":
            dp[i+1][1][1] += dp[i][j][1]
            dp[i+1][2][1] += dp[i][j][1]
            dp[i+1][0][0] += dp[i][j][1]
        else:
            dp[i+1][0][1] += dp[i][j][1]

print(sum(map(lambda x: sum(x) % MOD, dp[n])) % MOD) 
