
from math import gcd

K = int(input())

a = 0
for ai in range(1, K + 1):
  for bi in range(1, K + 1):
    gcd_ab = gcd(ai, bi)
    for ci in range(1, K + 1):
      a += gcd(gcd_ab, ci)

print(a)