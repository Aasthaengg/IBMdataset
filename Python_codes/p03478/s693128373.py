n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
  ii=list(str(i))
  ii=map(int,ii)
  ii=sum(ii)
  if a<=ii and b>=ii:
    ans+=i
print(ans)