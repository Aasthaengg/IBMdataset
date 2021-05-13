N = int(input())
P = [0.0] + list(map(float, input().split()))

dp = [[0.0 for _ in range(3002)] for _ in range(3002)]
dp[0][0] = 1

for i in range(1, N + 1):
  for j in range(3000):
    dp[i][j] = dp[i - 1][j - 1] * P[i] + dp[i - 1][j] * (1 - P[i])

answer = 0
for  j in range(N // 2 + 1, 3002):
  answer += dp[N][j]

print(answer)