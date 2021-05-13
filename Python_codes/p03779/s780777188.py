import numpy as np

X = int(input())
arr = np.arange(100000)
cumsum = arr.cumsum()
# print(cumsum[:5])
idx = np.searchsorted(cumsum, X)
print(idx)
