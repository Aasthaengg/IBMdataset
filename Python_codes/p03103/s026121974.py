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

n, m = map(int, input().split())
#print('m', m)
tmp = [None]*n
for i in range(n):
    tmp[i] = [None]*2
for i in range(n):
    tmp[i] = readints()
# print(tmp)
tmp_so = sorted(tmp, key=lambda x: x[0])
# print(tmp_so)
cnt = 0
cost = 0
for i in range(n):
    if tmp_so[i][1] <= m:
        m -= tmp_so[i][1]

        cost += tmp_so[i][1]*tmp_so[i][0]
    elif m <= tmp_so[i][1]:

        cost += m*tmp_so[i][0]
        m = 0
print(cost)
