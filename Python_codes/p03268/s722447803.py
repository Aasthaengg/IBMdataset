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
# https://atcoder.jp/contests/arc081/tasks/arc081_b
# D - Coloring Dominoes
"""
need to consider the case that ticket is not enough to lower everything
"""


def calc(num):
    return num**3


N = gi()
K = gi()

num = N // K
ans = calc(num)

if (K % 2 == 0):
    if N % K >= K // 2:
        num += 1
    ans += calc(num)

print(ans)
