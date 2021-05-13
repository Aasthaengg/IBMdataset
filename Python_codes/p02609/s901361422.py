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

def popcount(n):
    cnt = 0
    while n > 0:
        cnt += n & 1
        n //= 2
    return cnt
def f(n):
    cnt = 0
    while n != 0:
        n = n % popcount(n)
        cnt += 1
    return cnt

N = int(input())
X = input()
ones = X.count('1')
MOD1 = ones + 1
MOD2 = ones - 1
pow1 = [1] * (len(X) + 1)
pow2 = [1] * (len(X) + 1)
if MOD2 != 0:
    for i in range(1, len(X) + 1):
        pow1[i] = (pow1[i - 1] * 2) % MOD1
        pow2[i] = (pow2[i - 1] * 2) % MOD2
else:
    for i in range(1, len(X) + 1):
        pow1[i] = (pow1[i - 1] * 2) % MOD1

X1, X2 = 0, 0
for i in range(N):
    if X[i] == '1':
        X1 += pow1[N - i - 1]
        X2 += pow2[N - i - 1]
X1 %= MOD1
if MOD2 != 0:
    X2 %= MOD2

for i in range(N):
    d = N - i - 1
    if X[i] == '0':
        x = (X1 + pow1[d]) % MOD1
        print(f(x) + 1)
    else:
        if MOD2 != 0:
            x = (X2 - pow2[d]) % MOD2
            print(f(x) + 1)
        else:
            print(0)