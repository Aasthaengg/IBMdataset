N,M=map(int,input().split())
E=[list(map(int,input().split())) for i in range(M)]
INF=10**12
D=[[INF]*N for i in range(N)]
for i in range(N):
  D[i][i]=0
for i in range(M):
  D[E[i][0]-1][E[i][1]-1]=E[i][2]
  D[E[i][1]-1][E[i][0]-1]=E[i][2]
for k in range(N):
  for i in range(N):
    for j in range(N):
      D[i][j]=min(D[i][j],D[i][k]+D[k][j])
P=0
for i in range(M):
  for j in range(N):
    if D[j][E[i][0]-1]+E[i][2]==D[j][E[i][1]-1] or D[j][E[i][1]-1]+E[i][2]==D[j][E[i][0]-1]:
      break
    if j==N-1:
      P+=1
print(P)