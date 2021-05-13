"""AtCoder."""

import math

a, b, h, m = [int(v) for v in input().split(' ')]


class Point:

    def __init__(self, r, v):
        self.r = r
        self.w = (2 * math.pi) / v

    def get_pos(self, t):
        wt = self.w * t
        return self.r * math.cos(wt), self.r * math.sin(wt)


p1 = Point(a, 12 * 60)
p2 = Point(b, 60)

minute = (h * 60) + m
x1, y1 = p1.get_pos(minute)
x2, y2 = p2.get_pos(minute)

print(math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))
