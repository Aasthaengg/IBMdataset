import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
abs_A = abs(A)

min_A = min(abs_A)

if (A < 0).sum() % 2:
    print(sum(abs_A) - min_A * 2)
else:
    print(sum(abs_A))