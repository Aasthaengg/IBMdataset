import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    n, a, b = ns()

    h = [ni() for _ in range(n)]

    upper = 10 ** 9
    lower = 0

    while upper - lower > 1:
        mid = (upper + lower) // 2
        cnt = 0
        for hi in h:
            cnt += int(math.ceil(max(0, hi - b * mid) / (a - b)))
        if cnt <= mid:
            upper = mid
        else:
            lower = mid
    print(upper)


if __name__ == '__main__':
    main()
