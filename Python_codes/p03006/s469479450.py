N = int(input())
INF = int(1e13)
A = [list(map(int, input().split())) for _ in range(N)]
X = [[[0, 0] for __ in range(N)] for _ in range(N)]
for i in range(N):
  for j in range(N):
    X[i][j] = [A[i][0]-A[j][0], A[i][1] - A[j][1]]
for i in range(N):
  X[i][i][0], X[i][i][1] = INF + 2*i, INF + 2*i+1
D = {}
for i in range(N):
  for j in range(N):
    if X[i][j][0]*(10*INF)+X[i][j][1] in D:
      D[X[i][j][0]*(10*INF)+X[i][j][1]] += 1
    else:
      D[X[i][j][0]*(10*INF)+X[i][j][1]] = 1
if N == 1:
  print(1)
else:
  print(N-max(D[i] for i in D))
