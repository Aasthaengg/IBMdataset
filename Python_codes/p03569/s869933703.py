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

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    s = list(input())

    characters = []
    cnt = []
    counter = 0
    for si in s:
        if si != "x":
            characters.append(si)
            cnt.append(counter)
            counter = 0
        else:
            counter += 1
    cnt.append(counter)

    flg = True
    odd = len(characters) % 2
    for i in range(len(characters) // 2):
        if characters[i] != characters[-i - 1]:
            flg = False

    if not flg:
        print(-1)
        exit(0)

    ans = 0
    for i in range(len(cnt) // 2):
        ans += abs(cnt[i] - cnt[-i - 1])
    print(ans)


if __name__ == '__main__':
    main()
