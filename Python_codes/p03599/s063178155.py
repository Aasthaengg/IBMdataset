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

A, B, C, D, E, F = map(int, input().split())
if C > D:
    C, D = D, C

mx_rate = 0
ans_water = 0
ans_sugar = 0
for i in range(31):
    for j in range(31):
        total = (i * A + j * B) * 100
        if total > F:
            continue
        sugar_limit = min(F - total, (total // 100) * E)
        if sugar_limit > 0:
            for k in range(sugar_limit // C + 1):
                sugar_total = k * C
                if sugar_total < sugar_limit:
                    sugar_total += ((sugar_limit - sugar_total) // D) * D
                rate = 100 * sugar_total / (sugar_total + total)
                if rate >= mx_rate:
                    mx_rate = rate
                    ans_water = total + sugar_total
                    ans_sugar = sugar_total
print(ans_water, ans_sugar)

