import sys
input = sys.stdin.readline

N, T = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]

DP = [[[0] * 2 for _ in range(T)] for _ in range(2)]

a, b = AB[0]
if a < T:
  DP[0][a][0] = b
DP[0][0][1] = b

t = 1
for i in range(1, N):
  a, b = AB[i]
  if a < T:
    DP[t][a][0] = b
  DP[t][0][1] = b
  for j in range(T):
    DP[t][j][0] = max(DP[t][j][0], DP[1 - t][j][0])
    DP[t][j][1] = max(DP[t][j][1], DP[1 - t][j][1])
    if j + a < T: 
      DP[t][j + a][0] = max(DP[t][j + a][0], DP[1 - t][j][0] + b)
      DP[t][j + a][1] = max(DP[t][j + a][1], DP[1 - t][j][1] + b)
    DP[t][j][1] = max(DP[t][j][1], DP[1 - t][j][1])
    DP[t][j][1] = max(DP[t][j][1], DP[1 - t][j][0] + b)
  t = 1 - t
ans = 0
for i in range(T):
  ans = max(ans, DP[1 - t][i][0])
  ans = max(ans, DP[1 - t][i][1])

print(ans)