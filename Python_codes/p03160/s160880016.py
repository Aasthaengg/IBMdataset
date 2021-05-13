import sys
import numpy as np


def weight(n, hh):
    if n == 1:
        return 0
    if n == 2:
        return np.abs(hh[1] - hh[0])
    if n == 3:
        return min(np.abs(hh[2] - hh[1]) + np.abs(hh[1]-hh[0]), np.abs(hh[2] - hh[0]))
    else:
        weights = np.zeros(n).astype(int)
        weights[0] = 0
        weights[1] = np.abs(hh[1] - hh[0])
        weights[2] = min(np.abs(hh[2] - hh[1]) + np.abs(hh[1] - hh[0]), np.abs(hh[2] - hh[0]))

        for k in range(3, n):
          weights[k] = min(weights[k-2] + np.abs(hh[k] - hh[k-2]), weights[k-1]+ np.abs(hh[k] - hh[k-1]))
        return weights[n-1]


n = int(input())
svals = input()
hh = np.array(list(map(int, svals.rstrip(' ').split(' '))))
print(weight(n, hh))
