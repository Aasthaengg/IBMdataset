import sys
import re
import math
import collections
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===

def disLR(a, idx):
    small = a[max(0, idx - 1)]
    large = a[min(len(a) - 1, idx)]
    return small, large


def main():
    a, b, q = ns()
    s = [ni() for _ in range(a)]
    t = [ni() for _ in range(b)]

    for _ in range(q):
        ans = INF

        x = ni()
        tmpans = [0] * 4

        idxs = bisect.bisect_left(s, x)
        sml, lrg = disLR(s, idxs)
        tmpans[0] += abs(x - sml)
        tmpans[1] += abs(x - lrg)
        idxsml = bisect.bisect_left(t, sml)
        tmpans[0] += min([abs(sml - i) for i in disLR(t, idxsml)])
        idxlrg = bisect.bisect_left(t, lrg)
        tmpans[1] += min([abs(lrg - i) for i in disLR(t, idxlrg)])

        idxt = bisect.bisect_left(t, x)
        sml, lrg = disLR(t, idxt)
        tmpans[2] += abs(x - sml)
        tmpans[3] += abs(x - lrg)
        idxsml = bisect.bisect_left(s, sml)
        tmpans[2] += min([abs(sml - i) for i in disLR(s, idxsml)])
        idxlrg = bisect.bisect_left(s, lrg)
        tmpans[3] += min([abs(lrg - i) for i in disLR(s, idxlrg)])
        ans = min(ans, min(tmpans))
        print(ans)


if __name__ == '__main__':
    main()
