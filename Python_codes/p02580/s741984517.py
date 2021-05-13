import numpy as np
import numba
import sys
from numba import njit, b1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


@njit((i8, i8, i8[:]), cache=True)
def main(Height, Width, XY):
    UP = 300010
    row = np.zeros(UP, np.int64)
    col = np.zeros(UP, np.int64)
    
    for i in range(0, len(XY), 2):
        x, y = XY[i:i + 2] - 1
        row[x] += 1
        col[y] += 1
    
    row_max = row.max()
    col_max = col.max()

    judge = np.sum(row == row_max) * np.sum(col == col_max)

    for i in range(0, len(XY), 2):
        x, y = XY[i:i + 2] - 1
        
        if (row[x] == row_max and col[y] == col_max):
            judge -= 1
    
    summ = row_max + col_max
    
    return (summ if judge else summ - 1)


Height, Width, M_ko = map(int, readline().split())
XY = np.array(read().split(), np.int64)

ans = main(Height, Width, XY)
print(ans)
