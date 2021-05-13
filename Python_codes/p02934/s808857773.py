import numpy as np
n = int(input())
a = list(map(float, input().split()))
b = sum(np.reciprocal(a))
print(1/b)