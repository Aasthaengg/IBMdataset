from _collections import deque


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
import scipy
from collections import deque
from math import sqrt
from math import floor
#https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_c
#C - Align
"""
need to consider the case that ticket is not enough to lower everything
"""

N = gi()

hasO = 0

for i in range(N):
    a = gi()
    if (a % 2):
        hasO = 1

if hasO:
    print("first")
else:
    print("second")

#HLHL
