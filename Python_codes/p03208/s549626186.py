import numpy as np
n, k = map(int, input().split())
h = np.array(sorted([int(input()) for _ in range(n)]))
h_roll = np.roll(h, -k + 1)
x = h_roll - h
print(int(x[:-k + 1].min()))