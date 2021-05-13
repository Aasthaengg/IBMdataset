import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    x = i
    cnt = 0
    while i < K:
        i *= 2
        cnt += 1
    ans += (1 / N) * (1 / (2 ** cnt))
print(ans)

# def my_pow(base, n, mod):
#     if n == 0:
#         return 1
#     x = base
#     y = 1
#     while n > 1:
#         if n % 2 == 0:
#             x *= x
#             n //= 2
#         else:
#             y *= x
#             n -= 1
#         x %= mod
#         y %= mod
#     return x * y % mod