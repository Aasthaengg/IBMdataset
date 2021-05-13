import numpy as np
n,m = map(int, input().split())
arr = np.zeros(m)
for i in range(n):
    ka = np.array([int(i) for i in input().split()])
    for j in range(ka[0]):
        arr[ka[j+1]-1] += 1
ans = (arr == n).sum()
print(ans)