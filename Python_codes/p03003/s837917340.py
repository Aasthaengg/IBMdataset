N, M = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
MOD = 10**9 + 7
dp = [[0 for k in range(M+1)] for l in range(N+1)]

for k in range(N):
    for l in range(M):
        if S[k] == T[l]:
            dp[k+1][l+1] = dp[k+1][l] + dp[k][l+1] + 1
        else:
            dp[k+1][l+1] = dp[k+1][l] + dp[k][l+1] - dp[k][l]
        dp[k+1][l+1] %= MOD

print(dp[N][M]+1)
