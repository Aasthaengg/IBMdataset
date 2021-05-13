import sys
readline = sys.stdin.readline

N,M,Q = map(int,readline().split())
train = [[0] * (N + 1) for i in range(N + 1)]
for i in range(M):
  l,r = map(int,readline().split())
  train[l][r] += 1
  
for i in range(len(train)):
  for j in range(1,len(train[i])):
    train[i][j] = train[i][j] + train[i][j - 1]
    
for j in range(len(train)):
  for i in range(1,len(train[i])):
    train[i][j] = train[i - 1][j] + train[i][j]

for i in range(Q):
  p,q = map(int,readline().split())
  print(train[q][q] - train[p - 1][q] - train[q][p - 1] + train[p - 1][p - 1])
