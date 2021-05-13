import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math

MOD = 10 ** 9 + 7
# MOD = 998244353
# sys.setrecursionlimit(10**8)

x, y, a, b, c = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P = sorted(P, reverse=True)[:x]
Q = sorted(Q, reverse=True)[:y]
concat = P + Q + R
concat.sort(reverse=True)
print(sum(concat[:x+y]))