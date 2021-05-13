#!/usr/bin/env python3
n, *s = map(int, open(0).read().split())
v = list(map(lambda x: abs(x), s))
c = 0
for i in s:
    c += i < 0
if c % 2 == 0:
    print(sum(v))
else:
    print(sum(v) - 2*min(v))
