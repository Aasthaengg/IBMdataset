from sys import stdin
from math import gcd
for line in stdin:
    a, b = map(int, line.split())
    g = gcd(a, b)
    print(g, a // g * b)
