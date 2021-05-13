N = int(input())
K = int(input())

INF = 10**10

dp = [INF]*(N+1)
dp[0] = 1

for v in range(1,N+1):
    dp[v] = min(dp[v-1]*2,dp[v-1]+K)
print(dp[N])