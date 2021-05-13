import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions
import functools
import copy

# import heapq
# from collections import deque
# import decimal

sys.setrecursionlimit(10000001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))

# ===CODE===
tMOD = 998244353


def main():
    n = ni()
    a = na()

    tmp = []
    state = 0
    ans = 0
    for i in range(n):
        if len(tmp) < 1:
            hoge=0
        else:
            current_state = a[i]-tmp[-1]
            if current_state == 0:
                hoge=0
            elif state == 0:
                if current_state > 0:
                    state = 1
                else:
                    state = -1
            elif state * current_state < 0:
                tmp.clear()
                ans += 1
                state=0
        tmp.append(a[i])

    print(ans+1)


if __name__ == '__main__':
    main()
