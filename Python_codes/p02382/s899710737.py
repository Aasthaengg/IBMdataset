# -*- coding: utf-8 -*-

import sys
import os
import math

def distance(v0, v1, p):
    n = len(v0)
    s = 0
    for i in range(n):
        diff = abs(v0[i] - v1[i])
        s += diff ** p
    return s ** (1/p)

def chebyshev(v0, v1):
    n = len(v0)
    ret = 0
    for i in range(n):
        diff = abs(v0[i] - v1[i])
        if diff > ret:
            ret = diff
    return ret

n = int(input())
v0 = list(map(float, input().split()))
v1 = list(map(float, input().split()))

print(distance(v0, v1, 1))
print(distance(v0, v1, 2))
print(distance(v0, v1, 3))
print(chebyshev(v0, v1))