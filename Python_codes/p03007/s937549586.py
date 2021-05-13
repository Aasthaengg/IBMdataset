from _collections import deque
from _ast import Num


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def gw():
    global input_parser
    return next(input_parser)


def gi():
    data = gw()
    return int(data)


MOD = int(1e9 + 7)

import numpy
from collections import deque
from math import sqrt
from math import floor
#https://atcoder.jp/contests/arc091/tasks/arc091_b
#D - Remainder Reminder
"""
if has negative

if all positive

"""

N = gi()
A = [0] * N
ans = 0
max_vi = -1
max_v = -1e4 - 1
min_vi = -1
min_v = 1e4 + 1
for i in range(N):
    a = gi()
    A[i] = a
    if (a >= max_v):
        max_vi = i
        max_v = a
    if (a < min_v):
        min_vi = i
        min_v = a
    ans += abs(a)

seq = []
for i in range(N):
    if i == max_vi or i == min_vi:
        continue
    a = A[i]
    if a >= 0:
        seq.append((min_v, a))
        min_v -= a
    else:
        seq.append((max_v, a))
        max_v -= a
print(max_v - min_v)
for p in seq:
    print("%d %d" % (p[0], p[1]))
print(max_v, min_v)
