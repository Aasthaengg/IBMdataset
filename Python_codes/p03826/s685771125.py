import numpy as np
A, B, C, D = map(int, input().split())
S = np.array([A*B, C*D])
print(S.max())