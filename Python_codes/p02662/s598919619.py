N, S = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353
dp = [[0]*(S+1) for i in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(S+1):
        dp[i+1][j] = dp[i][j]*2
        if A[i] <= j:
            dp[i+1][j] += dp[i][j-A[i]]
        dp[i+1][j] %= mod
print(dp[N][S])