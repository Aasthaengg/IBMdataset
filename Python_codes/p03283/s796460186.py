n,m,q = map(int,input().split())

M = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
  l,r = map(int,input().split())
  M[r][l] += 1
  
D = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
  for j in range(1,n+1):
    D[i][j] = M[i][j] + D[i][j-1] + D[i-1][j] - D[i-1][j-1]
    
for i in range(q):
  p,q = map(int,input().split())
  ans = D[q][q] - D[q][p-1] - D[p-1][p] + D[p-1][p-1]
  print(ans)  