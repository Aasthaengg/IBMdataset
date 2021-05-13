import itertools
import itertools
import os
import sys
from collections import deque

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

H, W = list(map(int, sys.stdin.readline().split()))
S = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
seen = np.zeros((H, W), dtype=bool)

ans = 0
for h, w in itertools.product(range(H), range(W)):
    if seen[h][w]:
        continue
    que = deque()
    que.append((h, w))
    black = white = 0
    while que:
        h, w = que.popleft()
        if seen[h][w]:
            continue
        seen[h][w] = True
        if S[h][w] == '#':
            black += 1
        else:
            white += 1
        for dh, dw in zip((h + 1, h - 1, h, h), (w, w, w + 1, w - 1)):
            if 0 <= dh < H and 0 <= dw < W and not seen[dh][dw]:
                if S[h][w] != S[dh][dw]:
                    que.append((dh, dw))
    ans += black * white
print(ans)
