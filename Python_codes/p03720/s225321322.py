import numpy as np
n, m = map(int, input().split())

mat = [[0] * n] * n
mat = np.array(mat)

for i in range(m):
    a, b = map(int, input().split())

    mat[a - 1, b - 1] += 1
    mat[b - 1, a - 1] += 1


# print(mat)
for i in range(n):
    ans = np.sum(mat[i, :])
    print(ans)
