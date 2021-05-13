# -*- coding: utf-8 -*-

import math

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
abs_xy = []

for i in range(n):
    abs_xy.append(abs(x[i] - y[i]))

d1 = sum(abs_xy)

d2 = 0
for i in range(n):
    d2 += abs_xy[i] * abs_xy[i]
d2 = math.sqrt(d2)

d3 = 0
for i in range(n):
    d3 += abs_xy[i] * abs_xy[i] * abs_xy[i]
d3 = math.pow(d3, 1/3)

d = max(abs_xy)

print(d1)
print(d2)
print(d3)
print(d)
