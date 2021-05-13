import sys
import math
import collections
import bisect
import copy
import itertools

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
    n = ni()
    a = [ni() for _ in range(n)]
    ans = 0

    prev = -1
    for i, ai in enumerate(reversed(a)):
        if ai > n - i - 1:
            print(-1)
            exit(0)

        if i == 0:
            ans += ai
        else:
            if ai != prev - 1:
                if ai > prev - 1:
                    ans += ai
                else:
                    print(-1)
                    exit(0)
        prev = ai
    print(ans)

if __name__ == '__main__':
    main()
