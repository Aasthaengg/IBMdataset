import math
import string
import collections
from collections import Counter
from collections import deque
from decimal import Decimal
import sys
import fractions
from operator import itemgetter
import itertools


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
a, b, c = map(int, input().split())
for i in range(10**5):
    ans = a*i
    if ans % b == c:
        print('YES')
        exit()
print('NO')
