n = int(input())
t = [int(input()) for _ in range(n)]

import fractions
n = t[0]
for a,b in zip(t, t[1:]):
    g = fractions.gcd(n, b)
    n = n*b//g
print(n)