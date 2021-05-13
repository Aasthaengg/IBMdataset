#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
2

output:
0.00000000 0.00000000
11.11111111 0.00000000
16.66666667 9.62250449
22.22222222 0.00000000
33.33333333 0.00000000
38.88888889 9.62250449
33.33333333 19.24500897
44.44444444 19.24500897
50.00000000 28.86751346
55.55555556 19.24500897
66.66666667 19.24500897
61.11111111 9.62250449
66.66666667 0.00000000
77.77777778 0.00000000
83.33333333 9.62250449
88.88888889 0.00000000
100.00000000 0.00000000
"""

import sys
import math


class Point(object):
    __slots__ = ('x', 'y')

    def __init__(self, x=-1, y=-1):
        """
        Initialize the point
        """
        self.x = float(x)
        self.y = float(y)


def koch_curve(d, p1, p2):
    if not d:
        return None

    s, t, u = (Point() for _ in range(3))

    s.x = (2 * p1.x + p2.x) / 3
    s.y = (2 * p1.y + p2.y) / 3

    t.x = (p1.x + 2 * p2.x) / 3
    t.y = (p1.y + 2 * p2.y) / 3

    u.x = (t.x - s.x) * COS_60 - (t.y - s.y) * SIN_60 + s.x
    u.y = (t.x - s.x) * SIN_60 + (t.y - s.y) * COS_60 + s.y

    koch_curve(d - 1, p1, s)
    print('{0:.8f} {1:.8f}'.format(s.x, s.y))

    koch_curve(d - 1, s, u)
    print('{0:.8f} {1:.8f}'.format(u.x, u.y))

    koch_curve(d - 1, u, t)
    print('{0:.8f} {1:.8f}'.format(t.x, t.y))

    koch_curve(d - 1, t, p2)


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    depth = int(_input[0])
    SIN_60, COS_60 = math.sin(math.pi / 3), math.cos(math.pi / 3)

    p1_start, p2_end = Point(x=0, y=0), Point(x=100, y=0)
    print(format(p1_start.x, '.8f'), format(p1_start.y, '.8f'))
    koch_curve(depth, p1_start, p2_end)
    print(format(p2_end.x, '.8f'), format(p2_end.y, '.8f'))