N,M,Q=map(int,input().split())
L,R=0,0
A=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
  L,R=map(int,input().split())
  A[L][R]+=1
C=[[0]*(N+1) for i in range(N+1)]
for i in range(1,N+1):
  for j in range(1,N+1):
    C[i][j]=C[i][j-1]+C[i-1][j]-C[i-1][j-1]+A[i][j]
for i in range(Q):
  L,R=map(int,input().split())
  print(C[N][R]-C[L-1][R])