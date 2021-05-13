n,m,qu = map(int,input().split())
lr = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
  l,r = map(int,input().split())
  lr[l][r]+=1

for i in range(1,n+1):
  for j in range(i,n+1):
    lr[i][j]+=lr[i][j-1]
  
for i in range(1,n+1):
  for j in range(i):
    lr[i-j-1][i]+=lr[i-j][i]
    
for i in range(qu):
  p,q = map(int,input().split())
  print(lr[p][q])
