import numpy as np

n = int(input())
d, x = map(int, input().split())
a = np.array([int(input()) for _ in range(n)])
a = np.ceil(d / a)
print(int(np.sum(a) + x))