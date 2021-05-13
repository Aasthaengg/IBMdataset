import numpy as np

N = int(input())
A = [int(x) for x in input().split()]

A_rot = np.array(list(enumerate(A, 1))).T.astype(np.float128)
theta = np.pi / 4
R = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]], dtype=np.float128)
A_rot = np.dot(R, A_rot).T
loss = np.abs(A_rot[:, 1] - np.median(A_rot[:, 1])).sum()
print(int(np.round(np.sqrt(2) * loss)))