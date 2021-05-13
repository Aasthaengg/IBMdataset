from fractions import gcd
from functools import reduce
n=int(input())
g=1
for i in range(n):
  t=int(input())
  g=g*t//gcd(g,t)
print(g)
