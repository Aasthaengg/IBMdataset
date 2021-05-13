import sys
import re
import math
import collections
import decimal
import bisect

# import copy
# import heapq
# from collections import deque
# import decimal

# sys.setrecursionlimit(100001)
INF = sys.maxsize
# MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    a, b, c = ns()

    flg = a**2+b**2+c**2-2*a*b-2*a*c-2*b*c>0 and -a - b + c > 0

    print("Yes" if flg else "No")


if __name__ == '__main__':
    main()
