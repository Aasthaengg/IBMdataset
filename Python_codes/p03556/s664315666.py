import numpy as np
n = int(input())
for i in range(n, 0, -1):
    if np.sqrt(i) % 1 == 0:
        print(i)
        break