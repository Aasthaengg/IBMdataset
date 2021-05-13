N, K = map(int, input().split())
h = list(map(int, input().split()))
inf = float('inf')
dp = [inf] * N
dp[0] = 0

for i in range(N-1):
  for j in range(1, K+1):
    if i+j < N:
      dp[i+j] = min(dp[i]+abs(h[i]-h[i+j]), dp[i+j])

print(dp[N-1])