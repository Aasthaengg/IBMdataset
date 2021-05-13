n,m,Q=map(int,input().split())
mat=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
  l,r=map(int,input().split())
  mat[l][r]+=1

for i in range(n+1):
  for j in range(n+1):
    mat[i][j]+=mat[i-1][j]
    mat[i][j]+=mat[i][j-1]
    mat[i][j]-=mat[i-1][j-1]

for i in range(Q):
  p,q=map(int,input().split())
  s=mat[q][q]-mat[q][p-1]-mat[p-1][q]+mat[p-1][p-1]
  print(s)
