N, M, Q = map(int, input().split())
train = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  train[a][b] += 1
  
for i in range(1, N+1):
  for j in range(1, N+1):
    train[i][j] += train[i][j-1]
    
for i in range(1, N+1):
  for j in range(1, N+1):
    train[j][i] += train[j-1][i]


for i in range(Q):
  l, r = map(int, input().split())
  print(train[r][r]-train[l-1][r]-train[r][l-1]+train[l-1][l-1])