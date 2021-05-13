n=int(input())
if n==0 or n%2==1:
  print(0)
else:
  k=n//2
  s=5
  ans=0
  while k>=s:
    ans+=k//s
    s*=5
  print (ans)