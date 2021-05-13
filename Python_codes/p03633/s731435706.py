import math
n=int(input());a=[int(input()) for _ in range(n)];r=a[0]
for i in a:
  r=r*i//math.gcd(r,i)
print(r)