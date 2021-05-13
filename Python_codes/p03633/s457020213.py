import math
n,*t = map(int,open(0).read().split())
def lcm(a,b):
  return a*b//math.gcd(a,b)
if n == 1:
  print(t[0])
else:
  ans = lcm(t[0],t[1])
  for i in range(2,n):
    ans = lcm(ans,t[i])
  print(ans)