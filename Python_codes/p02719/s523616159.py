n,k=[int(x) for x in input().split()]
if n%k==0:
  print(0)
else:
  m=n//k
  a=abs(n-m*k)
  b=abs(a-k)
  ans=min(a,b)
  print(ans)