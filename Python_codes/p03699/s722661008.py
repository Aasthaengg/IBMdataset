#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
s = sum(a)
if s % 10 > 0:
    print(s)
else:
    m = sorted(i for i in a if i % 10 > 0)
    if len(m):
        print(s - m[0])
    else:
        print(0)
