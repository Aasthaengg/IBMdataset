# import bisect
from collections import Counter, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = int(input())

    CONST = 10**9

    if s % CONST != 0:
        a = CONST
        d = math.ceil(s/CONST)
        b = CONST - (s % CONST)
        c = 1
    else:
        a = CONST
        b = 0
        c = CONST
        d = s // CONST

    print(0, 0, a, b, c, d)

if __name__ == '__main__':
    main()