import numpy as np

n = int(input())
t, a = map(float, input().split())
h = np.array([float(x) for x in input().split()])

dif = np.abs(a - (t - 0.006 * h))
print(np.argmin(dif) + 1)
