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

N, M = map(int, input().split())

if abs(N - M) > 1:
    print(0)
    exit()

def f(n):
    ret = 1
    while n > 1:
        ret *= n
        ret %= MOD
        n -= 1
    return ret

ans = 1
ans *= f(N)
ans *= f(M)
if N == M:
    ans *= 2
print(ans % MOD)