import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W = map(int, readline().split())

tile = [0 for i in range(H)]
cnt = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    tile[i] = readline().decode().strip()

for i in range(H):
    done = [False for _ in range(W)]
    for j in range(W):
        if tile[i][j] == '#':
            continue
        if done[j]:
            continue
        l = 0
        while (j + l < W):
            if tile[i][j + l] == '#':
                break
            l += 1
        for k in range(l):
            cnt[i][j + k] += l
            done[j + k] = True

for j in range(W):
    done = [False for _ in range(H)]
    for i in range(H):
        if tile[i][j] == '#':
            continue
        if done[i]:
            continue
        l = 0
        while (i + l < H):
            if tile[i + l][j] == '#':
                break
            l += 1
        for k in range(l):
            cnt[i + k][j] += l
            done[i + k] = True

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(cnt[i][j] - 1, ans)
print(ans)

