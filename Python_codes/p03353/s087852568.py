import sys

import bisect
# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
from operator import attrgetter, itemgetter

# import math

# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    k = int(input())
    l = len(s)

    strs = set()

    for i in range(l):
        for j in range(k):
            if (i + j) < l:
                strs.add(s[i:i + j + 1])

    strl = list(strs)
    strl.sort()

    print(strl[k - 1])


if __name__ == '__main__':
    main()
