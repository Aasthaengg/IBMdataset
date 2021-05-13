from sys import stdin, setrecursionlimit
#input = stdin.buffer.readline
setrecursionlimit(10 ** 7)

from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, combinations_with_replacement
from itertools import accumulate
from math import ceil, sqrt, pi, radians, sin, cos

MOD = 10 ** 9 + 7
INF = 10 ** 18

K = int(input())
S = input()

len_S = len(S)

#MOD = 10 ** 9 + 7
SIZE = 2 * 10 ** 6 + 100
g1, g2, inv = [1, 1], [1, 1], [0, 1]
for i in range(2, SIZE + 1):
    g1.append((g1[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    g2.append((g2[-1] * inv[-1]) % MOD)
def nCr(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % MOD

answer = 0
for i in range(K + 1):
    answer += pow(25, i, MOD) * nCr(len_S - 1 + i, i) * pow(26, K - i, MOD)
    answer %= MOD

print(answer)