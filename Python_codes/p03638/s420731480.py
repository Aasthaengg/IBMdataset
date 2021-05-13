import numpy as np
H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

c = []
for i, j in enumerate(a):
    c += [i + 1] * j
c = np.array(c).reshape(H, W)

for i in range(1, H, 2):
    c[i, :] = c[i, ::-1]

for r in range(H):
    row = c[r, :]
    print(*row, sep=' ')
