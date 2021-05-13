import numpy as np

x = int(input())
is_p = np.array([True] * (2*x+1))

for i in range(2, 2*x+1):
    if is_p[i]:
        is_p[i::i] = False
        if i >= x:
            print(i)
            exit()