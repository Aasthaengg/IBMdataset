N,M,Q=map(int,input().split())
L,R=0,0
X=[[0]*N for i in range(N)]
for i in range(M):
  L,R=map(int,input().split())
  X[L-1][R-1]+=1
Y=[[0]*(N+1) for i in range(N+1)]
for i in range(N):
  for j in range(N):
    Y[i+1][j+1]=X[i][j]+Y[i+1][j]+Y[i][j+1]-Y[i][j]
for i in range(Q):
  L,R=list(map(int,input().split()))
  print(Y[N][R]-Y[L-1][R])