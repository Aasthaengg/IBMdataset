k = int(input())

from math import gcd

s = 0
for a in range(1, k+1):
  for b in range(1, k+1):
    g = gcd(a, b)
    for c in range(1, k+1):
      s += gcd(g, c)

print(s)
