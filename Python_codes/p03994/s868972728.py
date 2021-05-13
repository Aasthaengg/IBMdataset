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
    s = list(input())
    k = ni()

    for i in range(len(s)):
        if s[i] == "a":
            continue
        si = ord(s[i]) - 97
        if k >= 26 - si:
            s[i] = "a"
            k -= 26 - si
            if k == 0:
                break

    s[-1] = chr(97 + (ord(s[-1]) - 97 + k) % 26)

    print(*s, sep="")


if __name__ == '__main__':
    main()
