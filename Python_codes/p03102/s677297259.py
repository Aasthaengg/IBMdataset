import numpy as np

n, m, c = map(int, input().split())
b = np.array(list(map(int, input().split())))
arr = np.array([list(map(int, input().split())) for _ in range(n)])

result = (arr * b).sum(axis=1) + c
print(np.where(result > 0)[0].shape[0])