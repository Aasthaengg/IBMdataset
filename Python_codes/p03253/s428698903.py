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

fact = []

X = M
i = 2
while i ** 2 <= X:
    v = 0
    while M % i == 0:
        M //= i
        v += 1
    if v != 0:
        fact.append(v)
    i += 1
if M != 1:
    fact.append(1)

MAX = 2 * 10 ** 5
MOD = 10 ** 9 + 7

fac = [0 for i in range(MAX)]
finv = [0 for i in range(MAX)]
inv = [0 for i in range(MAX)]

def comInit(mod):
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod


def com(n, r, mod):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod
    
comInit(MOD)


ans = 1
for f in fact:
    ans *= com(f + N - 1, N - 1, MOD)
    ans %= MOD
print(ans)
