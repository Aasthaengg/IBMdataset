import numpy as np
K = int(input())
q, r = divmod(K, 50)
print(50)
print(*(np.array([100 - r] * r + [49 - r] * (50 - r)) + q))
