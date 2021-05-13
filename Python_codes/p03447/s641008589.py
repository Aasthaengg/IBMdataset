from heapq import heappush, heappop
from itertools import permutations, accumulate, combinations
import math
import bisect
import numpy as np
from collections import defaultdict, deque
from operator import itemgetter
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
# MOD = 10 ** 9 + 7
# INF = float("inf")


def main():
    x = int(input())
    a = int(input())
    ans = x -a
    b = int(input())
    ans = ans - (ans // b) * b
    print(ans)

if __name__ == '__main__':
    main()