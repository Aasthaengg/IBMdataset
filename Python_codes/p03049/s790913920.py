import bisect
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
    n = int(input())
    b_count = 0
    a_count = 0
    b_and_a_count = 0
    ans = 0

    for i in range(n):
        s = sys.stdin.readline().rstrip("\n")
        len_s = len(s)
        for j in range(len_s-1):
            if s[j] == "A":
                if s[j+1] == "B":
                    ans += 1
        if s[0] == "B" and s[-1] == "A":
            b_and_a_count += 1
        elif s[0] == "B":
            b_count += 1
        elif s[-1] == "A":
            a_count += 1

    if b_and_a_count > 0:
        ans += (b_and_a_count-1)
        if a_count > 0:
            ans += 1
            a_count -= 1
        if b_count > 0:
            ans += 1
            b_count -= 1

    ans += min(a_count, b_count)
    print(ans)

if __name__ == '__main__':
    main()