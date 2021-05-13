N, MA, MB = list(map(int, input().split()))
abc = [list(map(int, input().split())) for _ in range(N)]

inf = 1000 * N
M = N * 10 + 1
DP = [[[inf] * M for _ in range(M)] for _ in range(N)]

a, b, c = abc[0]
DP[0][a][b] = c

for i in range(1, N):
  a, b, c = abc[i]
  DP[i][a][b] = min(DP[i - 1][a][b], c)
  for j in range(M - 10):
    for k in range(M - 10):
      DP[i][j][k] = min(DP[i][j][k], DP[i - 1][j][k])
      if DP[i - 1][j][k] < inf:
        jj = j + a
        kk = k + b
        DP[i][jj][kk] = min(DP[i - 1][jj][kk], DP[i - 1][j][k] + c)
ans = inf
i = MA
j = MB
while i < M and j < M:
  ans = min(ans, DP[-1][i][j])
  i += MA
  j += MB

if ans == inf:
  print(-1)
else:
  print(ans)
