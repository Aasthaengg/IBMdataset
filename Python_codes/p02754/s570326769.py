n,a,b=map(int,input().split())
if a==0 and b==0:
  print(0)
else:
  c=n//(a+b)
  d=n%(a+b)
  m=min(a,d)
  ans=c*a+m
print(ans)