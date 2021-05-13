# coding=utf-8
from math import sqrt
x1, y1, x2, y2 = map(float, raw_input().split())
print sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)