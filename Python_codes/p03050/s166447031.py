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
# https://atcoder.jp/contests/arc067/tasks/arc067_a
# C - Factors of Factorial
"""
m > n impossible
m = n, possible only when n = 1


"""

N = gi()
ans = 0

for l in range(1, floor(sqrt(N)) + 1):
    if N % l:
        continue

    m = N // l

    if m < l - 1:
        ans += l - 1
    if l < m - 1:
        ans += m - 1

print(ans)
