import math
from fractions import gcd
a, b = map(int, input().split())
g = gcd(a, b)
sqrt = math.floor(g ** 0.5)
factors = [1]
z = g
for i in range(2, sqrt + 1):
    if not z % i:
        factors.append(i)
        while z % i == 0:
            z //= i
if z > 1:
    factors.append(z)
print(len(factors))
