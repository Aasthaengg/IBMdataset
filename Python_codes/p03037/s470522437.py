import numpy as np

i = list(map(int, input().split()))
N = i[0]
M = i[1]

l = np.array([list(map(int, input().split())) for i in range(M)])

limit1 = max(l[:, 0])
limit2 = min(l[:, 1])

print(max(limit2 - limit1 + 1, 0))