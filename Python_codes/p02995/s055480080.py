from math import gcd
a, b, c, d = map(int, input().split())
lcm = c * d // gcd(c, d)

x = (a - 1) - (a - 1) // c - (a - 1) // d + (a - 1) // lcm
y = b - b // c - b // d + b // lcm

print(y - x)