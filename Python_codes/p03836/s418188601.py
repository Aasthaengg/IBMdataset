import sys

# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue
import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    sx, sy, tx, ty = ns()

    ans = []

    ans.extend(["U"] * (ty - sy))
    ans.extend((["R"] * (tx - sx)))
    ans.extend(["D"] * ((ty - sy)))
    ans.extend((["L"] * (tx - sx)))

    ans.extend(["L"])

    ans.extend(["U"] * (ty - sy + 1))
    ans.extend((["R"] * (tx - sx + 1)))

    ans.extend(["DR"])

    ans.extend(["D"] * ((ty - sy + 1)))
    ans.extend((["L"] * (tx - sx + 1)))

    ans.extend(["U"])

    print(*ans, sep="")


if __name__ == '__main__':
    main()
