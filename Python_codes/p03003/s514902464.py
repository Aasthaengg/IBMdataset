N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
mod = 10**9+7

dp = [[0 for i in range(M)] for j in range(N)]
sum_dp = [[0 for i in range(M)] for j in range(N)]


if S[0] == T[0]:
    dp[0][0] = 1
    sum_dp[0][0] = 1

for i in range(1, N):
    if S[i] == T[0]:
        dp[i][0] = 1
    sum_dp[i][0] = (sum_dp[i-1][0] + dp[i][0])%mod

for j in range(1, M):
    if S[0] == T[j]:
        dp[0][j] = 1
    sum_dp[0][j] = (sum_dp[0][j-1] + dp[0][j])%mod

for i in range(1, N):
    for j in range(1, M):
        if S[i] == T[j]:
            dp[i][j] = (sum_dp[i-1][j-1] + 1)%mod
        sum_dp[i][j] = (sum_dp[i-1][j] + sum_dp[i][j-1] - sum_dp[i-1][j-1] + dp[i][j])%mod

print((sum_dp[N-1][M-1]+1)%mod)