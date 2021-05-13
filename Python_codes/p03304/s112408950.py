n,m,d=map(int,input().split())
if d==0:
  ans1=1/n*(m-1)
  print(ans1)
else:
  ans=0
  ans+=(m-1)*(n-d)/(n**2)
  print(ans*2)