MOD = int(1e9) + 7
M = int(1e9) + 7
L = input()
N = len(L)
dp = [[0] * 2 for i in range(N+5)]
dp[0][0] = 1
for i in range(N):
    nd = int(L[i])
    for j in range(2):
        ni = i+1
        nj = j
        if j == 0:
            if nd == 0:
                dp[ni][nj] = dp[i][j]
            else:
                dp[ni][nj] = (dp[i][j] * 2) % MOD
                dp[ni][1] += dp[i][j]
        else:
            dp[ni][nj] += dp[i][j] * 3
            dp[ni][nj] %= MOD
print((dp[N][0] + dp[N][1]) % MOD)
