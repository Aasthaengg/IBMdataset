import numpy as np
n, m = map(int, input().split())
A = np.array(list(map(int, input().split())))
print("Yes" if np.sum(A >= np.sum(A)/(4*m)) >= m else "No")
