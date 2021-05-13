import numpy as np

H, W = map(int, input().split())
N = int(input())
A = map(int, input().split())

canvas = np.zeros((H * W, ), dtype=np.object)
idx = 0

for color, a in enumerate(A):
    for _ in range(a):
        canvas[idx] = str(color + 1)
        idx += 1

for r, row in enumerate(canvas.reshape((H, W))):
    print(" ".join(row if not r % 2 else row[::-1]))