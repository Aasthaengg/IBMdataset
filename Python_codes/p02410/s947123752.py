#ITP1_6_D
n,m=map(int,input().split())
A=[[0 for j in range(m)]for i in range(n)]
B=[[0 for j in range(1)]for i in range(m)]
C=[[0 for j in range(1)]for i in range(n)]
for i in range(n):
  D=list(map(int,input().split()))
  for j in range(m):
    A[i][j]=D[j]
for i in range(m):
  B[i][0]=int(input())
S=int(0)
for j in range(n):
  for i in range(m):
    S=S+(A[j][i]*B[i][0])
  C[j][0]=S
  S=0
for i in range(n):
  print(C[i][0])

