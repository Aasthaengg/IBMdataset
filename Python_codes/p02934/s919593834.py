import numpy as np

N = int(input())

A = np.array(input().split(), dtype=np.float64)
ans = 1 / (1/A).sum()

print(ans)