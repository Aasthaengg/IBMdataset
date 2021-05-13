import numpy as np

n, k = map(int, input().split())
arr = np.array(list(map(int, input().split())))

# グループ内（初項）
a = 0
for i in range(n - 1):
    a += np.where(arr[i + 1:] < arr[i])[0].shape[0]

# グループ間（差）
d = 0
for i in range(n):
    d += np.where(arr < arr[i])[0].shape[0]

mod = 10**9 + 7

ans = (a + a + d * (k - 1)) * k // 2 % mod

print(ans)