import numpy as np
n = int(input())
a = np.array([int(i) for i in input().split()])
x = np.abs(a - a.mean())
print(np.argmin(x))