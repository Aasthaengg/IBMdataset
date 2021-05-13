import numpy as np

H, W, A, B = map(int, input().split())

grid = np.zeros((H, W), np.int8)
grid[:, :A] ^= 1
grid[:B] ^= 1

print('\n'.join(''.join(row) for row in grid.astype(str)))