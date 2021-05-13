#!/usr/bin/env python3
a, b, c = map(int, open(0).read().split())
if b//a >= c:
    print(c)
else:
    print(b//a)
