import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
# import math
from fractions import gcd

MOD = 10 ** 9 + 7
# MOD = 998244353
# sys.setrecursionlimit(10**8)


n, m = map(int, input().split())
A = list(map(int, input().split()))


def lcm_base(x, y):
    # return (x * y) // math.gcd(x, y)
    return (x * y) // gcd(x, y)


def lcm_list(numbers):
    x = 1
    for i in range(n):
        x = lcm_base(x, numbers[i])
        if x > 2*m:
            print(0)
            exit()

    return x


def count_two(x):
    count = 0
    while x%2 == 0:
        count += 1
        x //= 2
    return count


two_count = count_two(A[0])
for a in A[1:]:
    if two_count != count_two(a):
        print(0)
        exit()

LCM = lcm_list(A)
# print(LCM)
print((m - LCM//2)//LCM + 1)
