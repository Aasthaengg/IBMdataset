import numpy as np

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
XY = np.array(xy).flatten()

X = XY[::2] ; Y = XY[1::2]

dx = X[:,None] - X[None, :]
dy = Y[:, None] - Y[None,:]

dist_mat = (dx*dx + dy*dy) ** .5

answer = dist_mat.sum() / N
print(answer)
