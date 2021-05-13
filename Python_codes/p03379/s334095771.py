#!/usr/bin/env python3
n, *x = map(int, open(0).read().split())
s = sorted(x)
m1 = s[n // 2 - 1]
m2 = s[n // 2]
for i in x:
    if i < m2:
        print(m2)
    else:
        print(m1)
