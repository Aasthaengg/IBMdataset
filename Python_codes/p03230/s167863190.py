import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

MOD = 10 ** 4 + 7

N = int(input())
if N == 1:
    print("Yes")
    print(2)
    print(1, 1)
    print(1, 1)
    exit()
i = 1
K = 0
while i ** 2 <= 2 * N:
    if i * (i + 1) == 2 * N:
        K = i + 1
        break
    i += 1

if K == 0:
    print("No")
    exit()

print("Yes")
print(K)
ladder = [i for i in range(1, K - 1)]
start = 1
base = [start]
for l in ladder:
    base.append(base[-1] + l)
for i in range(K - 1):
    num = K - 1
    s = [base[i]]
    for j in range(i):
        s.append(s[0] + j + 1)
    for j in range(i + 1, K - 1):
        s.append(base[j] + i)
    print(K - 1, *s)
diagnal = [1]
for l in ladder[1:] + [K - 1]:
    diagnal.append(diagnal[-1] + l)
print(K - 1, *diagnal)