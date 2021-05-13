import numpy as np

Cij = [list(input()) for _ in range(2)]
Cij_inv = np.rot90(Cij, 2)

if np.array_equal(Cij, Cij_inv):
    print('YES')
else:
    print('NO')