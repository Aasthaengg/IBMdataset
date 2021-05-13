H,W,D=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]
Q=int(input())
L,R=[],[]
for i in range(Q):
  L.append(list(map(int,input().split())))
  R.append(L[i][1])
  L[i]=L[i][0]
B=dict()
for i in range(H):
  for j in range(W):
    B[A[i][j]]=(i,j)
C=[[0,0] for i in range(D)]
for i in range(1,D):
  for j in range(i+D,H*W+1,D):
    C[i].append(C[i][-1]+abs(B[j][0]-B[j-D][0])+abs(B[j][1]-B[j-D][1]))
for j in range(D+D,H*W+1,D):
  C[0].append(C[0][-1]+abs(B[j][0]-B[j-D][0])+abs(B[j][1]-B[j-D][1]))
for i in range(Q):
  print(C[R[i]%D][(R[i]+D-1)//D]-C[L[i]%D][(L[i]+D-1)//D])