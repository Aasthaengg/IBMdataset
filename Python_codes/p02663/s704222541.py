from copy import deepcopy
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
import copy


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

h1, m1, h2, m2, k = map(int, input().split())
ans = (h2-h1)*60
ans += m2-m1
ans -= k
print(ans)
