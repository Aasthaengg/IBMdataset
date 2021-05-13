n,a,b,*x=map(int,open(0).read().split())
ans=0
for i in range(1,n):
  ans+=min((x[i]-x[i-1])*a,b)
print(ans)