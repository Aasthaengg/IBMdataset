import sys
import math
import collections
import bisect
import copy

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, m = ns()
    d = []
    for _ in range(m):
        a, b = ns()
        d.append([a - 1, b - 1])

    d.sort(key=lambda x: x[1])

    down = -1
    ans = 0
    for a, b in d:
        if down < a:
            down = b-1
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
