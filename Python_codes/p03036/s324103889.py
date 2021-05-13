import sys

# import bisect
# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
from operator import attrgetter, itemgetter

# import math

# from numba import jit
# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    r, d, x1 = list(map(int, readline().split()))

    xc = x1
    for i in range(10):
        xc = xc * r - d
        print(xc)


if __name__ == '__main__':
    main()
