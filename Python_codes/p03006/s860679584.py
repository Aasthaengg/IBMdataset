import sys

# import re
import math
import collections
# import decimal
import bisect
# import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    pos = []
    for i in range(n):
        x, y = ns()
        pos.append((x, y))

    res = dict()
    for i in range(n):
        for j in range(n):
            if i == j: continue
            tmp_key = (pos[j][0] - pos[i][0], pos[j][1] - pos[i][1])
            if tmp_key in res.keys():
                res[tmp_key].append((pos[i], pos[j]))
            else:
                res[tmp_key] = [(pos[i], pos[j])]

    ans = 0
    for k in res.keys():
        ans = max(ans, len(res[k]))

    print(n-ans)


if __name__ == '__main__':
    main()
