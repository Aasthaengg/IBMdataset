H,W,D=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]
Q=int(input())
B=[list(map(int,input().split())) for _ in range(Q)]
L,R=zip(*B)
C=[[]for i in range(H*W)]
for i in range(H):
  for j in range(W):
    a=A[i][j]
    C[a-1]=((j+1,i+1))
X=[0]*(H*W+1)
for i in range(D):
  x=H*W-D-i
  count=0
  while x>0:
    count+=abs(C[x-1][0]-C[x+D-1][0])+abs(C[x-1][1]-C[x+D-1][1])
    X[x]+=count
    x-=D
for i in range(Q):
  print(X[L[i]]-X[R[i]])