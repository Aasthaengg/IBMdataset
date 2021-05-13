n,m,k=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
ca=[0]*(n+1)
ca[1]=a[0]
for i in range(n):
  ca[i+1]=ca[i]+a[i]
cb=[0]*(m+1)
cb[1]=b[0]
for i in range(m):
  cb[i+1]=cb[i]+b[i]
j=m
ans=0
for i in range(n+1):
  t=ca[i]
  while j>=0:
    if t+cb[j]>k:
      j-=1
    else:
      ans=max(ans,i+j)
      break
print(ans)