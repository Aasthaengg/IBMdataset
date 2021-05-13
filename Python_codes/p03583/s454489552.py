import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
import numpy as np


n = int(input())
U = 3500
for x in range(1, U+1):
    y = np.arange(1, U+1, dtype=np.int64)
    den = 4 * x * y - n * x - n * y
    num = n * x * y
    y = y[(num % den == 0) & (den > 0)]
    if len(y) > 0:
        y = y[0]
        z = (n * x * y) // (4 * x * y - n * x - n * y)
        break
print(x, y, z)
