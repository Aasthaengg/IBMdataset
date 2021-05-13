import numpy as np
from itertools import product
import sys
read = sys.stdin.buffer.read


C = np.array(read().split(), np.int32).reshape(3, 3)

a, b, c = np.max(C + 1, axis=1)
N = []
for i, j in product(range(a), range(b)):
    x = C[0, :] - i
    y = C[1, :] - j

    if np.all(x == y):
        N.append(x)

flag = 0
z = C[2, :]
for n in N:
    for k in range(c):
        if np.all(z - k == n):
            flag = 1
            break
    
    if flag:
        break

print(['No', 'Yes'][flag])