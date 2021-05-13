#!/usr/bin/env python3
n, t, a, *h = map(int, open(0).read().split())
h = list(map(lambda x: abs(a-(t-x*0.006)), h))
a = list(enumerate(h))
a.sort(key=lambda x: x[1])
print(a[0][0]+1)
