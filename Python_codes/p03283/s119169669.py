N, M, Q = map(int, input().split())
X = [[0 for _ in range(N+1)] for __ in range(N+1)]
for i in range(M):
  L, R = map(int, input().split())
  X[L][R] += 1
for i in range(N+1):
  for j in range(N):
    X[i][j+1] += X[i][j]
for i in range(N+1):
  for j in range(N):
    X[j+1][i] += X[j][i]
for i in range(Q):
  p, q = map(int, input().split())
  print(X[q][q] - X[p-1][q])