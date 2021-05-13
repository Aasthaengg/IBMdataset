#!/usr/bin/env python3
_, c, k, *t = map(int, open(0).read().split())
t.sort()
n = 0
f = t.pop(0)
p = 1
for i in t:
    if i > f + k or p >= c:
        n += 1
        p = 1
        f = i
    else:
        p += 1
print(n + 1)
