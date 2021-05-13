#!/usr/bin/env python

def sqroot(n):
    x = 1
    for i in range(100):
        x = (x + n/x)/2
    return x

x1, y1, x2, y2 = input().split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

distance = sqroot((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

print("%.8f" % distance)