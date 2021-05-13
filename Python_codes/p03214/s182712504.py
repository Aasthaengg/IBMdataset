import numpy as np
n = int(input())
l = np.array([int(i) for i in input().split()])

mean = np.mean(l)

l = np.abs(l - mean)

print(np.where(l == l.min())[0][0])
