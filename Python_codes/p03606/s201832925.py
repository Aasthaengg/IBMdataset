import numpy as np
N = int(input())
seat = np.zeros(1000000, dtype=int)
L, R = np.array([input().split() for _ in range(N)], dtype=int).T

np.add.at(seat, L, 1)
np.add.at(seat, R+1, -1)
np.cumsum(seat, out=seat)
print(seat.sum())