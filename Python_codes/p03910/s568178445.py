n = int(input())

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...
# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ...

A = [0] * (n + 1)
A[1] = 1 
for i in range(1, n):
    A[i + 1] = A[i] + i

from bisect import bisect_left

idx = bisect_left(A, n)

if n == A[idx]:
    for i in range(1, idx + 1):
        if i == idx - 1: continue
        print(i)
else:
    for i in range(1, idx):
        if i == idx - 1 - (n - A[idx - 1] + 1): continue
        print(i)