# coding: utf-8
import sys
from itertools import accumulate

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W, K = lr()
S = [list(map(int, sr())) for _ in range(H)]
Scum = [list(accumulate(row)) for row in S]
# H方向はbit全探索、W方向はGreedyに
INF = 10 ** 10
answer = INF
for pattern in range(1<<(H-1)):
    slice = set()
    cnt = 0
    for i in range(H-1):
        if pattern>>i & 1:
            slice.add(i)
            cnt += 1
    slice.add(H-1)  # 最後の区切り
    w = 0
    prev = -1
    while w < W:
        cut = False
        white = 0
        for i in range(H):
            white += Scum[i][w] - (Scum[i][prev] if prev >= 0 else 0)
            if i in slice:
                if white > K:
                    cut = True
                    break
                white = 0
        if cut:
            if prev == w - 1:  # 1列でKをオーバーしたので無理
                break
            cnt += 1
            prev = w-1
        else:
            w += 1
    else:
        answer = min(answer, cnt)

print(answer)
# 43