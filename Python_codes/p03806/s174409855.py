import sys
input = sys.stdin.buffer.readline

N, Ma, Mb = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]

sumA = sum([ABC[i][0] for i in range(N)])
sumB = sum([ABC[i][1] for i in range(N)])

INF = 10 ** 15
dp = [[INF for j in range(sumB + 1)] for i in range(sumA + 1)]
dp[0][0] = 0

for a, b, c in ABC:
  for i in range(sumA, -1, -1):
    for j in range(sumB, -1, -1):
      if dp[i][j] != INF:
        dp[i + a][j + b] = min(dp[i + a][j + b], dp[i][j] + c)

answer = INF
for i in range(1, sumA + 1):
  for j in range(1, sumB + 1):
    if dp[i][j] != INF and i / j == Ma / Mb:
      answer = min(answer, dp[i][j])
      
print(answer if answer != INF else -1)