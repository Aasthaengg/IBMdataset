import numpy as np
H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

c = []
for i, j in enumerate(a):
    c += [i + 1] * j
c = np.array(c).reshape(H, W)
c[1::2, :] = c[1::2, ::-1]

for r in range(H):
    row = c[r, :]
    print(*row, sep=' ')
