import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
 
sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

MOD = 10 ** 9 + 7
N, K = map(int, input().split())
count = Counter()
for i in reversed(range(1, K + 1)):
    c = pow(K // i, N, MOD)
    j = 2
    while i * j <= K:
        c -= count[i * j]
        j += 1
    count[i] = c
print(sum(i * j for i, j in count.items()) % MOD)
