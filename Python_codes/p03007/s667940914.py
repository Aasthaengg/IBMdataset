import sys
from collections import defaultdict, deque
import bisect
from heapq import *
from math import factorial, ceil, floor
from collections import defaultdict
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# N, M, = map(int, input().split())
# N = int(input())
# L = [int(v) for v in input().split()]
# L = [[int(v) for v in input().split()] for _ in range(N)]
# L = [int(input()) for _ in range(N)]
# L = [list(input().strip())  for _ in range(N)]
# S = input().strip()

N, = map(int, input().split())
L = [int(v) for v in input().split()]
L.sort()

# only + 2
# only - 1
# + - 3
c = 0
for v in L:
    if v < 0:
        c = c | 1
    elif v > 0:
        c = c | 2

if c == 0:
    c = 2

if c == 2:
    if N == 2:
        print(max(L) - min(L))
        print(max(L), min(L))
        exit()

    ans = []
    p = L[0] - L[-1]
    ans.append((L[0], L[-1]))
    for v in L[1:-2]:
        ans.append((p, v))
        p -= v
    ans.append((L[-2], p))
    print(L[-2] - p)
    for x, y in ans:
        print(x, y)

if c == 1:
    if N == 2:
        print(max(L) - min(L))
        print(max(L), min(L))
        exit()

    ans = []
    p = L[-1] - L[0]
    ans.append((L[-1], L[0]))
    for v in L[1:-2]:
        ans.append((p, v))
        p -= v
    ans.append((p, L[-2]))
    print(p - L[-2])
    for x, y in ans:
        print(x, y)

if c == 3:
    if N == 2:
        print(max(L) - min(L))
        print(max(L), min(L))
        exit()

    mc = 0
    for v in L:
        if v < 0:
            mc += 1

    ans = []
    if N - mc == 1:
        p = L[-1] - L[0]
        ans.append((L[-1], L[0]))
        for v in L[1:-1]:
            ans.append((p, v))
            p -= v
        print(p)
        for x, y in ans:
            print(x, y)

        exit()

    ans = []
    p = L[0] - L[-1]
    ans.append((L[0], L[-1]))
    for v in L[mc:-2]:
        ans.append((p, v))
        p -= v
    ans.append((L[-2], p))
    p = L[-2] - p
    for v in L[1:mc]:
        ans.append((p, v))
        p -= v
    print(p)
    for x, y in ans:
        print(x, y)