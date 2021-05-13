import numpy as np
H, W, M = map(int, input().split())

C = [0] * W
R = [0] * H
S = set()
for _ in range(M):
    h, w = map(int, input().split())
    h, w = h - 1, w - 1  # 0-indexed
    C[w] += 1
    R[h] += 1
    S.add((h, w))

col_max = max(C)
col_idx = [i for i in range(W) if C[i] == col_max]
row_max = max(R)
row_idx = [i for i in range(H) if R[i] == row_max]

ans = col_max + row_max
for r in row_idx:
    for c in col_idx:
        if not (r, c) in S:
            print(ans)
            exit()
print(ans - 1)
