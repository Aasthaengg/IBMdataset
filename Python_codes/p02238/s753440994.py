import sys
import math
import string
import fractions
import random
from operator import itemgetter
import itertools
from collections import deque
import copy
import heapq
import bisect

MOD = 10 ** 9 + 7
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

sys.setrecursionlimit(10 ** 8)

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
ans = [[i + 1, -1, -1] for i in range(n)]
check = [0 for _ in range(n)]
time = 1


def dfs(num):
    check[num] = 1
    global time
    if ans[num][1] == -1:
        ans[num][1] = time
        time += 1
    for i in info[num][2:]:
        if check[i - 1] == 0:
            dfs(i - 1)
    if ans[num][2] == -1:
        ans[num][2] = time
        time += 1


for i in range(n):
    if check[i] == 0:
        dfs(i)

for i in ans:
    i = list(map(str, i))
    print(" ".join(i))

