import numpy as np

A, B, C, K = map(int, input().split(" "))
vec = np.array([[A], [B], [C]])
mat = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
mat = np.linalg.matrix_power(mat, K)
ans = mat.dot(vec)

if abs(ans[0] - ans[1]) <= 10e18:
    print(int(ans[0] - ans[1]))
else:
    print('Unfair')
