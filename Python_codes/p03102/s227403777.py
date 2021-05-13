import numpy as np
n, m, c = map(int, input().split())
B = np.array(list(map(int, input().split())))
A = np.array([list(map(int, input().split())) for _ in range(n)])

print(((A * B).sum(axis=1) + c > 0).sum())