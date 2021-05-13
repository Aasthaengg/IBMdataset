import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N + 1):
  for j in range(M + 1):
    dp[i][j] = i * M + j * N - 2 * i * j
    if dp[i][j] == K:
      print("Yes")
      exit(0)
print("No")