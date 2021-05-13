#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18

N = input()
A = [-INF] + sorted(map(int, raw_input().split())) + [INF]
B = sorted(map(int, raw_input().split()))
C = [-INF] + sorted(map(int, raw_input().split())) + [INF]

ans = 0

pos1 = 0
pos2 = 0

for num in B:
    while A[pos1] < num:
        pos1 += 1
    pos1 -= 1
    while C[pos2] <= num:
        pos2 += 1
    pos2 -= 1
    ans += pos1 * (N - pos2)

print ans