n,k=map(int,input().split())
ans=0
for a in range(1,n+1):
  m=(k-a-1)%k+1
  if (m+m)%k!=0:continue
  ans+=((n-m+k)//k)*((n-m+k)//k)
print(ans)