import numpy as np

N = int(input())
A = list(map(int, input().split()))

A_sorted = np.argsort(A)

print(*A_sorted+1)