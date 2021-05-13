import math

n=int(input())
a=[int(input()) for _ in range(n)]
if n==1:
  print(a[0])
elif n==2:
  print(a[0]*a[1]//math.gcd(a[0],a[1]))
else:
  r=a[0]*a[1]//math.gcd(a[0],a[1])
  for i in a:
    r=r*i//math.gcd(r,i)
  print(r)