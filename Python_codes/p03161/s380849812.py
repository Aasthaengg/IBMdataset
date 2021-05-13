import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
H = list(map(int,readline().split()))

INF = 10 ** 10
dp = [INF] * N
dp[0] = 0

for i in range(N - 1):
  for j in range(1, K + 1):
    if i + j >= N:
      break
    if dp[i + j] > dp[i] + abs(H[i + j] - H[i]):
      dp[i + j] = dp[i] + abs(H[i + j] - H[i])
      
print(dp[N - 1])