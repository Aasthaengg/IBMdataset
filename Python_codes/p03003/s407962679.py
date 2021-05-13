N,M = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
MOD = 10**9+7

dp = [[1]*(M+1) for i in range(N+1)]

for i,s in enumerate(S):
    for j,t in enumerate(T):
        if s==t:
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
        else:
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j]
        dp[i+1][j+1] %= MOD
print(dp[-1][-1])