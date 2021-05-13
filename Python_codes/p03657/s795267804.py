import numpy as np


a, b = map(int ,input().split())
l = np.array([a, b, a+b])
l %= 3
if all(l):
    print("Impossible")
else:
    print("Possible")
