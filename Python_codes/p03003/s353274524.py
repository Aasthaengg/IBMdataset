MOD = 10**9 + 7

N, M = map(int, input().split())
Ss = list(map(int, input().split()))
Ts = list(map(int, input().split()))

dp = [[1]*(M+1) for _ in range(N+1)]
for i, S in enumerate(Ss, 1):
    for j, T in enumerate(Ts, 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        if S != T:
            dp[i][j] -= dp[i-1][j-1]
        dp[i][j] %= MOD

print(dp[-1][-1])
