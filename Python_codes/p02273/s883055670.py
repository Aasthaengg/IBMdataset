#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin
from math import pi, sin, cos

COS_PI_3 = cos(pi / 3.0)
SIN_PI_3 = sin(pi / 3.0)


def koch_curve(s, e, n):
    if not n:
        return (s, e)
    x = (e[0]-s[0]) / 3.0
    y = (e[1]-s[1]) / 3.0
    p1 = (s[0] + x, s[1] + y)
    p2 = (x*COS_PI_3 - y*SIN_PI_3 + p1[0], x*SIN_PI_3 + y*COS_PI_3 + p1[1])
    p3 = (e[0] - x, e[1] - y)
    return (koch_curve(s, p1, n-1) + koch_curve(p1, p2, n-1)[1:] +
            koch_curve(p2, p3, n-1)[1:] + koch_curve(p3, e, n-1)[1:])


n = int(stdin.readline())
for x, y in koch_curve((0, 0), (100, 0), n):
    print('{:.8f} {:.8f}'.format(x, y))