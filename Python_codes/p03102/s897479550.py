import numpy as np

N, M, C = map(int, input().split())
B = np.array(list(map(int, input().split())))
A = np.array([])
count = 0
for _ in range(N):
    A = np.append(A, list(map(int, input().split())))
A = A.reshape(N, M)
for i in A.dot(B) + C:
    if i > 0:
        count += 1
print(count)