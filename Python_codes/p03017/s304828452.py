# import bisect
# from collections import Counter, defaultdict, deque, namedtuple
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    n, a, b, c, d = list(map(int,ipti().split()))
    a -= 1
    b -= 1
    c -= 1
    d -= 1

    s = input()

    if c > d:
        s_groupby = itertools.groupby(s[b-1:d+2])
        for key, group in s_groupby:
            group_list = list(group)
            if key == "." and len(group_list) >= 3:
                break
        else:
            print('No')
            sys.exit()

    for i in range(a + 1, d):
        if s[i] == "#":
            if s[i + 1] == "#":
                print('No')
                sys.exit()

    print('Yes')

if __name__ == '__main__':
    main()
