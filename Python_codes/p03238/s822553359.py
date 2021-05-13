from heapq import heappush, heappop
from itertools import permutations, accumulate, combinations
from math import pi, ceil, floor
import numpy as np
from collections import defaultdict, deque
from operator import itemgetter
from bisect import bisect_left, bisect_right, insort_left, insort_right
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
# MOD = 10 ** 9 + 7
# INF = float("inf")


def main():
    n = int(input())
    if n == 1:
        print("Hello World")
    else:
        a = int(input())
        b = int(input())
        print(a + b)

if __name__ == '__main__':
    main()