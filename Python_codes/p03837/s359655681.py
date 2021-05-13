n,m=map(int,input().split())
G=[[10**18]*n for i in range(n)]
e=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    G[a-1][b-1]=c
    G[b-1][a-1]=c
    e.append([a-1,b-1,c])
for i in range(n):
  G[i][i]=0
for k in range(n):
  for i in range(n):
    for j in range(n):
      if G[i][j]>G[i][k]+G[k][j]:
        G[i][j]=G[i][k]+G[k][j]

print(sum(c>G[a][b] for a,b,c in e))