import sys
N=int(input())
A=list(map(int,input().split()))
if A[0]>=2:
  print(-1)
  sys.exit()
if A[0]==1:
  left=0
else:
  left=1
ans=A[N]
P=[1 for i in range(N+1)]
for i in range(1,N+1):
  point=left*2
  P[i]=point
  if point-A[i]<0:
    print(-1)
    sys.exit()
  left=point-A[i]
root=A[N]
for i in range(N,0,-1):
  root=min(P[i-1],root+A[i-1])
  ans+=root
print(ans)    