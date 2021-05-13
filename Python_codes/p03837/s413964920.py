N, M = map(int, input().split())
Map = [[int(1e18) for _ in range(N)] for __ in range(N)]
Path = [[[] for _ in range(N)] for __ in range(N)]
D = {}
for i in range(M):
  a, b, c = map(int, input().split())
  Map[a-1][b-1] = c
  Map[b-1][a-1] = c
  Path[a-1][b-1] = [a-1, b-1]
  Path[b-1][a-1] = [b-1, a-1]
  D[(a-1)*N+b-1] = 0
  D[(b-1)*N+a-1] = 0
for i in range(N):
  Map[i][i] = 0

for k in range(N):
  for i in range(N):
    for j in range(N):
      if Map[i][j] > Map[i][k] + Map[k][j]:
        Map[i][j] = Map[i][k] + Map[k][j]
        Path[i][j] = Path[i][k][:] + Path[k][j][1:]
        
for i in range(N):
  for j in range(N):
    X = Path[i][j][:]
    n = len(X)
    for k in range(n-1):
      l = X[k] * N + X[k+1]
      r = X[k+1] * N + X[k]
      if l in D:
        D[l] = 1
      if r in D:
        D[r] = 1
SUM41 = 0
for i in D:
  if D[i] == 0:
    SUM41 += 1
print(SUM41 // 2)