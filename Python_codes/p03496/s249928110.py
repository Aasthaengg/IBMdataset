import numpy as np
from collections import Counter

N = int(input())
A = list(map(int, input().split(" ")))

MIN = min(A)
MAX = max(A)

print(2 * N - 1)

if abs(MAX) > abs(MIN):
    index = np.argsort(A)[-1] + 1
    for i in range(1, N + 1):
        if i != index:
            print(index, i)
    print(index, index)
    for i in range(1, N):
        print(i, i + 1)
else:
    index = np.argsort(A)[0] + 1
    for i in range(1, N + 1):
        if i != index:
            print(index, i)
    print(index, index)
    for i in range(1, N)[::-1]:
        print(i + 1, i)