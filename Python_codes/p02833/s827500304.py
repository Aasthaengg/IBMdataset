n=int(input())

if n<2 or n%2==1:
  print(0)
else:
  ans=0
  now=10
  while(now<=n):
    ans+=n//now
    now*=5
  print(ans)