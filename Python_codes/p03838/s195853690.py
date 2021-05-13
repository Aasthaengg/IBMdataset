#!/usr/bin/env python3
x, y = map(int, input().split())
c = 0
if x * y < 0:
    x = abs(x)
    y = abs(y)
    c = 1

if y < x:
    print(1 + (y != 0 and x != 0) + x - y - c)
else:
    print(y - x + c)
