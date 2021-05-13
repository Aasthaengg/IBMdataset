import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions

import copy

# import heapq
# from collections import deque
# import decimal

sys.setrecursionlimit(10000001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    s = list(input())
    result = [s.count("a"), s.count("b"), s.count("c")]
    tmp = min(result)
    for i in result:
        if i - tmp > 1:
            print("NO")
            exit(0)

    print("YES")


if __name__ == '__main__':
    main()
