import numpy as np

n, l = map(int, input().split())
a = np.arange(1, n+1) + l - 1
print(np.sum(a) - a[np.argmin(np.abs(a))])
