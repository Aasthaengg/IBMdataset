from math import floor
import numpy as np

N = int(input())
K = floor((N * 2) ** 0.5)
if K * (K + 1) // 2 != N:
    print('No')
    exit()
else:
    print('Yes')
    print(K + 1)

grid = np.ones((K, K), np.int64)
grid[1:, 0] = np.arange(1, K)
grid[:, 0] = np.cumsum(grid[:, 0])
grid = np.cumsum(grid, axis=1).astype(str)
answer = []
k = str(K)
answer.append([k] + np.diag(grid).tolist())
answer.append([k] + grid[:, 0].tolist())
for i in range(1, K):
    answer.append([k] + grid[i, :i].tolist() + grid[i:, i].tolist())

print('\n'.join(map(' '.join, answer)))
