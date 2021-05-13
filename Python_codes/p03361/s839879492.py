# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W = lr()
S = [sr() for _ in range(H)]
bl = True
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            continue
        for dy, dx in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ny = i + dy
            nx = j + dx
            if 0 <= ny < H and 0 <= nx < W and \
                    S[ny][nx] == '#':
                break
        else:
            bl = False

print('Yes' if bl else 'No')
