import numpy as np
n = int(input())
a = np.array([[int(i) for i in input().split()] for _ in range(2)])
t = 0
for i in range(n):
    tmp = a[0, : i+1].sum() + a[1, i:].sum()
    t = max(t, tmp)
print(t)