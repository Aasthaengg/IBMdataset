import numpy as np

def fill_zeros_with_last(A):
    for i in range(len(A)):
        arr = A[i]
        prev = np.arange(arr.size)
        prev[arr == 0] = 0
        np.maximum.accumulate(prev, out=prev)
        A[i] = arr[prev]
    return A

H, W, K = map(int, input().split())
cake = np.zeros((H, W), dtype=int)
cnt = 1
for i in range(H):
    for j, S in enumerate(input()):
        if S == "#":
            cake[i][j] = cnt
            cnt += 1

for i in [1,2,3,2]:
    cake = np.rot90(cake, k=i)
    cake = fill_zeros_with_last(cake)

for c in cake:
    print(*c)