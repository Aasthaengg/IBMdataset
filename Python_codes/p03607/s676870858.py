#! /usr/bin/env python3

from fractions import gcd
# from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement

N = int(input())
A = [int(input()) for i in range(N)]

c = Counter(A)

ret = list(filter(lambda x: x % 2 == 1,  c.values()))

print(len(ret))
