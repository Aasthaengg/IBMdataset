N,M=map(int,input().split())
a,b,c=0,0,0
E=[]
INF=10**12
D=[[INF]*N for i in range(N)]
for i in range(N):
  D[i][i]=0
for i in range(M):
  a,b,c=map(int,input().split())
  a,b=a-1,b-1
  D[a][b]=c
  D[b][a]=c
  E.append((a,b,c))
for k in range(N):
  for i in range(N):
    for j in range(N):
      D[i][j]=min(D[i][j],D[i][k]+D[k][j])
P=0
for i in range(M):
  if D[E[i][0]][E[i][1]]!=E[i][2]:
    P+=1
print(P)