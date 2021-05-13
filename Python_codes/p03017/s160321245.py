import sys
import re
import math
import collections
import decimal
import bisect
import itertools

import copy

# import heapq
# from collections import deque
# import decimal

# sys.setrecursionlimit(100001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, a, b, c, d = ns()
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    s = list(input())

    stone_twice_flg = True
    for i in range(a, max(c, d)):
        if s[i] == s[i + 1] == "#":
            stone_twice_flg = False
            break

    pass_flg = False
    if c > d:
        for i in range(b, d+1):
            if s[i - 1] == s[i] == s[i + 1] == ".":
                pass_flg = True
                break
    else:
        pass_flg = True

    if stone_twice_flg and pass_flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
