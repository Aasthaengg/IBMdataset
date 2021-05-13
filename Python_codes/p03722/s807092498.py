n,m=map(int,input().split())
INF=float('inf')
G=[]
for _ in range(m):
  a,b,c=map(int,input().split())
  G.append([a-1,b-1,-c])

def bellmanFord(G,s):
  D=[INF for i in range(n)]
  D[s]=0
  for i in range(1,n):
    for x,y,z in G:
      D[y]=min(D[y],D[x]+z)
  ans=-D[n-1]
  for x,y,z in G:
    D[y]=min(D[y],D[x]+z)
  if ans!=-D[n-1]:
    return -1
  else:
    return -D[n-1]

ans=bellmanFord(G,0)
if ans==-1:
  print('inf')
else:
  print(ans)