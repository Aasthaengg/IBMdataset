W,H,N = map(int, input().split())
m = [[0]*W]*H
import numpy as np
arr = np.array(m)

for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        arr[:,:x] = 1
    if a == 2:
        arr[:, x:] = 1
    if a == 3:
        arr[H - y:,:] = 1
    if a == 4:
        arr[:H-y,:] = 1
print(np.count_nonzero(arr == 0))

