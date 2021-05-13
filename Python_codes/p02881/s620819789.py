import numpy as np
N = int(input())
x = np.arange(1, int(N ** 0.5 + 1))
div = x[N % x==0]
print(int(np.min(div + N / div)) - 2)