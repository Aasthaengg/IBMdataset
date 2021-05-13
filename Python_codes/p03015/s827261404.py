L = input()
N = len(L)
MOD = 10 ** 9 + 7

# dp[i][j]: (a,b)の組の個数
# i: 決定した桁数
# j: a + b < L[i] フラグ
dp = [[0] * 2 for _ in range(N + 1)]

dp[0][0] = 1

# 配るDP
for i in range(N):
    for j in range(2):
        # (a, b) = (0, 0)
        if int(L[i]): # 1
            dp[i + 1][1] = (dp[i + 1][1] + dp[i][j]) % MOD
        else: # 0
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
        
        # a ^ b = 1
        if int(L[i]) or j:
            dp[i+1][j] = (dp[i+1][j] + dp[i][j] * 2) % MOD

print(sum(dp[N]) % MOD)