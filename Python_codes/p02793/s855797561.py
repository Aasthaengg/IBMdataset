import bisect
import collections
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N = int(input())
A = list(map(int,(input().split())))

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def multiple(a, b):
    return a*b // euclid(a, b)

def lcm(nums):
        return functools.reduce(multiple, nums)

X = lcm(A)
ans = 0
for i in range(N):
    ans += X//A[i]
ans %= MOD
print(ans)