import numpy as np

W, H, N = map(int, input().split())

area = np.ones((W, H))

for _ in range(N):
    x, y, a = map(int, input().split())

    if a == 1:
        area[:x, :] = 0
    elif a == 2:
        area[x:, :] = 0
    elif a == 3:
        area[:, :y] = 0
    elif a == 4:
        area[:, y:] = 0

print(int(np.sum(area)))
