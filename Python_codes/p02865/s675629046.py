import numpy as np

n = int(input())

ar = np.array(range(1, (n // 2) + 1))


br = n - ar

# print(ar, br)
# print(ar != br)
print(np.count_nonzero(ar != br))
