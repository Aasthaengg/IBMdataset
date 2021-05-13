import numpy as np
from itertools import product

N = int(input())

points = []
non_zero_point = None
for _ in range(N):
    x, y, h = map(int, input().split(' '))
    points.append((x, y, h))
    if non_zero_point is None and h > 0:
        non_zero_point = (x, y, h)

points = np.array(points)
zeros = np.zeros(shape=N, dtype=np.int64)

for cx, cy in product(range(0, 101), repeat=2):
    H = abs(non_zero_point[0] - cx) + abs(non_zero_point[1] - cy) + non_zero_point[2]
    h = np.maximum(H - np.abs(points[:, 0] - cx) - np.abs(points[:, 1] - cy), zeros)
    if np.all(h == points[:, 2]):
        print(cx, cy, H)
        break
