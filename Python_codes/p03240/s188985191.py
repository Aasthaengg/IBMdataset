import sys
import numpy as np

n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]
xyh.sort(key=lambda x: x[2], reverse=True)

for cx in range(101):
    for cy in range(101):
        x, y, h = xyh[0]
        tmp_h = abs(cy - y) + abs(cx - x) + h
        H = np.zeros(n, dtype=np.bool)
        for i, a in enumerate(xyh):
            H[i] = a[2] == max(tmp_h - abs(cx - a[0]) - abs(cy - a[1]), 0)
        if np.all(H):
            print(cx, cy, tmp_h)
            sys.exit()