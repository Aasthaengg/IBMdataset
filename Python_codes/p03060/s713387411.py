import numpy as np

_ = int(input())
v = np.array(list(map(int, input().split())))
c = np.array(list(map(int, input().split())))

res = v - c
res = res[np.where(res > 0)]

print(res.sum())