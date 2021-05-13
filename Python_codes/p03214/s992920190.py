import numpy as np

n = int(input())
a = np.array(list(map(float,input().split())))

m = np.mean(a)

a -= m
a = np.abs(a)
print(np.argmin(a))