import math
import string
import collections
from collections import Counter
from collections import deque


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
n = int(input())
a1 = readints()
a2 = readints()
# print(a1)
# print(a2)
ans = 0
for i in range(n):
    tmp = 0
    tmp += sum(a1[:i+1])
    tmp += sum(a2[i:])
    ans = max(tmp, ans)
print(ans)
