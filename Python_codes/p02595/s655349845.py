import numpy as np
N, D = map(int, input().split())
p = np.array([list(map(int, input().split())) for i in range(N)])
dis = np.sqrt(p[:, 0]**2 + p[:, 1]**2)

print((dis <= D).sum())

