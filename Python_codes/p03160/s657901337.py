import numpy as np


def weight(n, hh):
    weights = np.zeros(n).astype(int)
    weights[0] = 0
    if n==1:
        return weights[0]
    weights[1] = np.abs(hh[1] - hh[0])
    if n==2:
        return weights[1]
    # weights[2] = min(np.abs(hh[2] - hh[1]) + np.abs(hh[1] - hh[0]), np.abs(hh[2] - hh[0]))

    for k in range(2, n):
      weights[k] = min(weights[k-2] + np.abs(hh[k] - hh[k-2]), weights[k-1]+ np.abs(hh[k] - hh[k-1]))
    return weights[n-1]


n = int(input())
svals = input()
hh = np.array(list(map(int, svals.rstrip(' ').split(' '))))
print(weight(n, hh))
