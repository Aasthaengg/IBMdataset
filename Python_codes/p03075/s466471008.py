import numpy as np
a = np.array([int(input()) for _ in range(5)])
k = int(input())

bl = a.max() - a.min() <= k

print("Yay!") if bl else print(":(")