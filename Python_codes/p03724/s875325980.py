import numpy as np

n, m = map(int, input().split())

arr = []
for _ in range(m):
    a, b = map(int, input().split())
    arr.append(a)
    arr.append(b)

arr = np.array(arr)

print("YES" if np.where(np.bincount(arr) % 2 != 0)[0].shape[0] == 0 else "NO")