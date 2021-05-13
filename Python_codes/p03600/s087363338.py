N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
for k in range(N):
  for i in range(N):
    for j in range(N):
      if A[i][j]>A[i][k]+A[k][j]:
        print(-1)
        exit()
INF=10**12
D=[[INF]*N for i in range(N)]
for i in range(N):
  D[i][i]=0
X=[]
for i in range(N):
  for j in range(N):
    if i==j:
      continue
    X.append([A[i][j],i,j])
P=0
X.sort()
for i in range(len(X)):
  for j in range(N):
    if X[i][0]==D[X[i][1]][j]+D[j][X[i][2]] and D[j][X[i][2]]!=0 and D[X[i][1]][j]!=0:
      break
    if j==N-1:
      P+=X[i][0]
  D[X[i][1]][X[i][2]]=X[i][0]
  D[X[i][2]][X[i][1]]=X[i][0]
print(P//2)