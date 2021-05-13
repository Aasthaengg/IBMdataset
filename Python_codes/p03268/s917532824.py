n,k=map(int,input().split())
ans=0
for a in range(1,n+1):
  b=c=(k-a-1)%k+1
  if (b+c)%k:continue
  ans+=((n-b)//k+1)**2
print(ans)