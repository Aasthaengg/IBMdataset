N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

INF = 10 ** 15
WF = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for a, b, c in ABC:
  WF[a][b] = c
  WF[b][a] = c
for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      WF[i][j] = min(WF[i][j], WF[i][k] + WF[k][j])

answer = 0
for a, b, c in ABC:
  if WF[a][b] < c:
    answer += 1
print(answer)