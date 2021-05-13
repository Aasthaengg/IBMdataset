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
N = int(input())

facts = [0] * (N + 1)
def f(n):
    i = 2
    while i ** 2 <= N:
        if n % i == 0:
            n //= i
            facts[i] += 1
        else:
            i += 1
    if n > 1:
        facts[n] += 1

for i in range(2, N + 1):
    f(i)
        
ans = 1
for i in range(2, N + 1):
    ans *= facts[i] + 1
    ans %= MOD
print(ans % MOD)
