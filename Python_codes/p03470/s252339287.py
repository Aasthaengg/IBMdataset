import numpy as np

N = int(input())
d = [input() for x in range(N)]

print(len(np.unique(np.array(d))))
