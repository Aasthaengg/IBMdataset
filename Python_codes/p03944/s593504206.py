import numpy as np
W, H, N = map(int, input().split())
g = np.zeros((H, W))

for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        g[:, :x] = 1
    elif a == 2:
        g[:, x:] = 1
    elif a == 3:
        g[abs(H-y):, :] = 1
    else:
        g[:abs(H-y), :] = 1

print(np.count_nonzero(g == 0))
