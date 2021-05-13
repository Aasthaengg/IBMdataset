from collections import Counter
import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))
u = np.unique(A)
if len(u) % 2 == 0:
    print(len(u) - 1)
else:
    print(len(u))
