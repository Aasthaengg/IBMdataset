N, M = map(int, input().split())
C = list(map(int, input().split()))

INF = 10**8
dp = [INF]*(N+1)
dp[0] = 0

for i in range(1, N+1):
    for j in range(M):
        if i < C[j]:
            continue
        dp[i] = min(dp[i], dp[i-C[j]]+1)
print(dp[-1])

