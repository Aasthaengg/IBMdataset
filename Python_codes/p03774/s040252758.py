import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M = MAP()
P = []
C = []
for i in range(N):
    a, b = MAP()
    P.append([a, b])
for j in range(M):
    c, d = MAP()
    C.append([c, d])

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for i in range(N):
    min_d = INF
    for j in range(M):
        tmp_d = calculate_manhattan_distance(P[i][0], P[i][1], C[j][0], C[j][1])
        if tmp_d < min_d:
            min_d = tmp_d
            ans_c_id = j + 1
    print(ans_c_id)
