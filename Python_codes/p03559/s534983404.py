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
    n = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))
    ans = 0
    for b in B:
        i = bisect_left(A, b)
        j = n - bisect_right(C, b)
        if i == 0 or j == 0:
            continue
        ans += i * j
    print(ans)



if __name__ == '__main__':
    main()