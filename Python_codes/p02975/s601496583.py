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
    n = ni()
    a = na()

    # p1
    if sum(a) == 0:
        print("Yes")
        exit(0)

    # p2
    c = collections.Counter(a)
    if n % 3 == 0:
        if 0 in c.keys() and len(c) == 2:
            if n // 3 == c[0]:
                print("Yes")
                exit(0)

    # p3

    t_key=[]
    t_value=[]
    if len(c) == 3:
        for k,v in c.items():
            t_key.append(k)
            t_value.append(v)
    else:
        print("No")
        exit(0)


    if t_key[0] ^ t_key[1] ^ t_key[2] == 0 and t_value[0]==t_value[1]==t_value[2]==n//3:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
