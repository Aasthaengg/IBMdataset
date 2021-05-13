import sys

import bisect

from collections import Counter, deque, defaultdict

# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math


# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    t = input()

    sd = defaultdict(list)

    sl = len(s)

    for i in range(sl):
        c = s[i]
        sd[c].append(i+1)

    tl = len(t)
    prev = 0

    ans = 0

    for i in range(tl):
        c2 = t[i]
        appear = sd[c2]
        if len(appear) == 0:
            print(-1)
            sys.exit()

        appear_max = appear[-1]
        if appear_max <= prev:
            nxt = appear[0]
        else:
            nxt = appear[bisect.bisect_right(appear, prev)]
        forward = nxt - prev
        if forward <= 0:
            forward += sl
        ans += forward
        prev = nxt

    print(ans)


if __name__ == '__main__':
    main()
