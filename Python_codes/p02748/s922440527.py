import numpy as np

lenA, lenB, M = map(int, input().split())

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
X = np.zeros((M, 3), dtype=int)

for i in range(M):
    X[i] = list(map(int, input().split()))

ans = min(A) + min(B)

for xi in X:
    tmp = A[xi[0] - 1] + B[xi[1] - 1] - xi[2]
    ans = min(ans, tmp)

print(ans)