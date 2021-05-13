import math
a,b,c=map(int,input().split())
d=math.gcd(a,b)
for i in range(d,0,-1):
  if d%i==0:
    c-=1
    if c==0:
      print(i)
      break