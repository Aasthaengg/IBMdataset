import itertools
import math
import string
import collections
from collections import Counter
from collections import deque
import sys
sys.setrecursionlimit(2*10**5)
INF = 2**60


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def has_duplicates2(seq):
    seen = []
    for item in seq:
        if not(item in seen):
            seen.append(item)
    return len(seq) != len(seen)


def divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor


# coordinates
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
S = input()
a = S.count('a')
b = S.count('b')
c = S.count('c')
if abs(a-b) <= 1 and abs(b-c) <= 1 and abs(a-c) <= 1:
    print('YES')
else:
    print('NO')
