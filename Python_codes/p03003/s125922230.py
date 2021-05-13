MOD = 10**9+7
N, M = map(int, input().split())
S = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    dp[i+1][0] = 1
for j in range(M):
    dp[0][j+1] = 1

for i, s in enumerate(S):
    for j, t in enumerate(T):
        if s == t:
            dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1]) % MOD
        else:
            dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1] - dp[i][j] + MOD) % MOD
print(dp[-1][-1])
