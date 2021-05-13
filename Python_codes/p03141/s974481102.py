import numpy as np

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split(' '))))

arr = np.array(arr)
arr = arr[np.argsort(np.sum(arr, axis=1))[::-1]]
takahashi = np.sum(arr[::2, 0], axis=0)
aoki = np.sum(arr[1::2, 1], axis=0)

print(takahashi - aoki)
