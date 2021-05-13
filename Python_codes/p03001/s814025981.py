import math
import string
import collections
from collections import Counter


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
W, H, x, y = map(int, input().split())
tmp = 0

if x*2 == W and y*2 == H:
    tmp = (W*H)/2
    print('{:f}'.format(tmp), 1)
    exit()
else:

    print('{:f}'.format((H*W)/2), 0)
    exit()
