import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np

N = int(input())

"""
4xyz = n(xy+yz+zx)
(4xy-ny-nx)z = nxy
"""

UP = 3501

for x in range(1, UP):
    y = np.arange(1, UP, dtype=np.int64)
    den = N * x * y
    num = 4*x*y - N*y - N*x
    y = y[(den % num == 0) & (num > 0)]
    if len(y) > 0:
        y = y[0]
        z = (N * x * y) // (4*x*y - N*y - N*x)
        break
print(x, y, z)