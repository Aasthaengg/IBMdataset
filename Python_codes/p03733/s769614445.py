import numpy as np
N, T = map(int, input().split())
t = np.array(input().split(), dtype=int)

dt = np.diff(t)
dt = np.minimum(dt, T)
print(T + dt.sum())