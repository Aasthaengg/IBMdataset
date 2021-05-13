#!/usr/bin/env python3
from itertools import combinations

H, W, K = map(int, input().split())
G_ = []

for i in range(H):
    G_.append(list(input()))

count = 0
g = 0
for cr in range(2**H):
    G = [G_[r][:] for r in range(H)]
    # row
    for r in range(H):
        if cr & (1 << r):
            G[r] = list('R' * W)
    # col
    for cc in range(2**W):
        G0 = [G[r][:] for r in range(H)]
        for c in range(W):
            if cc & (1 << c):
                for r in range(H):
                    G0[r][c] = 'R'
        b = sum(r.count("#") for r in G0)
        if b == K:
            count += 1
        g+=1
print(count)

