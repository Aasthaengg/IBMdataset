# Frog2
N, K = map(int, input().split())
h = list(map(int, input().split()))
inf = float("inf")
dp = [inf for _ in range(N)]
dp[0] = 0
for i in range(N):
    for j in range(1, K+1):
        if i + j >= N:
            break
        dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i+j]))
print(dp[-1])