#!/usr/bin/env python3
from math import gcd

n, m = map(int, input().split())
s, t = input(), input()
g = n * m // gcd(n, m)
if all(s[i * g // m] == t[i * g // n] for i in range(gcd(n, m))):
    print(g)
else:
    print(-1)
