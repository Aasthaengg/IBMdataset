import numpy as np
from itertools import product

h, w, k = map(int, input().split())
arr = np.empty((0, w), int)
for _ in range(h):
    s = list(input().replace(".", "0").replace("#", "1"))
    arr = np.append(arr, np.array([list(map(int, s))]), axis=0)
cnt = 0
for i in product((0, 1), repeat=h):
    tmp = (arr.T * i).T
    cnt += sum(sum(sum(tmp * j)) == k for j in product((0, 1), repeat=w))
print(cnt)