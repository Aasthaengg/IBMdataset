N, M = map(int, input().split())
C = list(map(int, input().split()))
INF = 10**9
dp = [INF]*(N+1)
dp[0] = 0
for i in range(M):
    for n in range(N+1):
        if n >= C[i]:
            dp[n] = min(dp[n], dp[n-C[i]]+1)
print(dp[N])
