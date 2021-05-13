H,W=map(int,input().split())
N=int(input())
A=list(map(int,input().split()))
a=[0 for i in range(H*W)]
b=[0 for i in range(N)]
b[0]=A[0]
for i in range(1,N):
  b[i]=b[i-1]+A[i]

for i in range(N):
  if i==0:
    for j in range(b[i]):
      a[j]=1
  else:
    for j in range(b[i-1],b[i]):
      a[j]=i+1
   
ans=[[0 for i in range(W)] for j in range(H)]
for i in range(H):
  for j in range(W):
    ans[i][j]=a[W*i+j]
for i in range(H):
  if i%2==1:
    ans[i].reverse()
  print(*ans[i])