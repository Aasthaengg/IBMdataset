import numpy as np
w, h, n, *Q = map(int, open(0).read().split())
B = np.ones((h, w), dtype=int)
for x, y, a in zip(Q[::3], Q[1::3], Q[2::3]):
    if a == 1:
        for i in range(x):
            B[:, i] = 0
    elif a == 2:
        for i in range(x, w):
            B[:, i] = 0
    elif a == 3:
        for i in range(y):
            B[i, :] = 0
    else:
        for i in range(y, h):
            B[i, :] = 0
print(np.sum(B))