INF = float('inf')
N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [INF] * N
dp[0] = 0

for i in range(1, N):
    for j in range(1, min(i, K) + 1):
        dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))

print(dp[N - 1])