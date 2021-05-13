import math
import string
import collections
from collections import Counter
from collections import deque
from decimal import Decimal
import sys
import fractions


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
ab = [0]*n
cd = [0]*m
for i in range(n):
    ab[i] = readints()
for i in range(m):
    cd[i] = readints()
# print(ab)
# print(cd)
x = []
for i in range(n):
    tmp_li = []
    ans = 10**100
    tmp = 0
    for j in range(m):
        tmp = abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1])
        # print(ab[i][0], cd[j][0], ab[i][1], cd[j][1])
        # print(i, j)
        tmp_li.append(tmp)
    # print(tmp_li)
    x.append(tmp_li.index(min(tmp_li)))
# print(x)
for i in range(len(x)):
    y = x[i]+1
    print(y)
