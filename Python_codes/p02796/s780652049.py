import sys

# import re
# import math
# import collections
# import decimal
# import bisect
# import itertools
# import fractions
# import functools
# import copy
# import heapq
# import decimal
# import statistics
# import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 10
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    d = [na() for _ in range(n)]

    query = []

    for i, di in enumerate(d):
        s = di[0] - di[1]
        t = di[0] + di[1]
        query.append((s, 1, i))
        query.append((t, 0, i))

    query.sort(key=lambda x: x[1])
    query.sort()

    ans = 0
    idx = -1
    for x, st, i in query:
        if st == 0:
            if idx == i:
                idx = -1
        if st == 1:
            if idx == -1:
                idx = i
            else:
                if d[idx][0] + d[idx][1] > d[i][0] + d[i][1]:
                    idx = i
                ans += 1

    print(n - ans)


if __name__ == '__main__':
    main()
