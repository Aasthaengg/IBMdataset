n,m=map(int,input().split())
x=[0]*m
for i in range(0,n):
  lis=list(map(int,input().split()))
  k=lis[0]
  for j in range(1,k+1):
    a=lis[j]-1
    x[a]+=1

ans=0
for y in x:
  if y==n:
    ans+=1
print(ans)