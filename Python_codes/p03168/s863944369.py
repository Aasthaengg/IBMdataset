import sys
input = sys.stdin.readline
N = int(input())
p = list(map(float, input().split()))
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
  for j in range(N + 1):
    if dp[i][j] == 0: continue
    dp[i + 1][j] += dp[i][j] * (1 - p[i])
    dp[i + 1][j + 1] += dp[i][j] * p[i]
res = 0
for j in range(N // 2 + 1, N + 1): res += dp[-1][j]
print(res)