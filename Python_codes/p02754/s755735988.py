n,a,b=map(int,input().split())
m=n//(a+b)
ans=a*m
if n-m*(a+b)>=a:
  ans+=a
else:
  ans+=n-m*(a+b)

print(ans)
