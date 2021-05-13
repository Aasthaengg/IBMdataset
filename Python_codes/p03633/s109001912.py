import math

a=[int(input()) for _ in range(int(input()))]
r=a[0]
for i in range(len(a)):
  r=r*a[i]//math.gcd(r,a[i])
print(r)