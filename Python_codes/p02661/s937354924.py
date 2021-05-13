N=int(input())
A=[0]*N
B=[0]*N
x,y=0,0
for i in range(N):
  x,y=map(int,input().split())
  A[i]=x
  B[i]=y
A.sort()
B.sort()
if N&1:
  print(B[N//2]-A[N//2]+1)
else:
  print(B[N//2]+B[N//2-1]-A[N//2]-A[N//2-1]+1)