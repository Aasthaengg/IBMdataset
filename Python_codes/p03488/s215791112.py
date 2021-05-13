import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    s = list(input())
    x, y = ns()

    axis = [[], []]

    cnt = 0
    sw = 0
    for si in s:
        if si == "F":
            cnt += 1
        else:
            axis[sw].append(cnt)
            cnt = 0
            sw ^= 1
    axis[sw].append(cnt)
    if len(axis[0]) > 0:
        x -= axis[0][0]
        del axis[0][0]

    x_cand = {0}
    y_cand = {0}

    for xi in axis[0]:
        if xi == 0:
            continue
        nxt = set()
        for xc in x_cand:
            nxt.add(xc + xi)
            nxt.add(xc - xi)
        x_cand = nxt

    for yi in axis[1]:
        if yi == 0:
            continue
        nxt = set()
        for yc in y_cand:
            nxt.add(yc + yi)
            nxt.add(yc - yi)
        y_cand = nxt

    if x in x_cand and y in y_cand:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
