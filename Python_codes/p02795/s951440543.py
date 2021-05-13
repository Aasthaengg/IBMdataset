import numpy as np

h = int(input())
w = int(input())
n = int(input())
x = max(h,w)
print(int(np.ceil(n/x)))