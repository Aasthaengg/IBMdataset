import numpy as np
N, M = (int(x) for x in input().split())
x, y, z = np.zeros(N, dtype=int), np.zeros(N, dtype=int), np.zeros(N, dtype=int)
for i in range(N):
    x[i], y[i], z[i] = (int(x) for x in input().split())
temp = []
for sx in (-1, 1):
    for sy in (-1, 1):
        for sz in (-1, 1):
            _x, _y, _z = sx*x, sy*y, sz*z
            T = np.sort(_x+_y+_z)[::-1][:M].sum()
            temp.append(T)

print(max(temp))
