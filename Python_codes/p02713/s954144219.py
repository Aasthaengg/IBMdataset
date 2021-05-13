import numpy as np
K = int(input())
k = np.arange(1,K+1, dtype=np.int64)
print(np.gcd.outer(np.gcd.outer(k,k),k).sum())