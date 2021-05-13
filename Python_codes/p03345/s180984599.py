import numpy as np
# -*- coding: utf-8 -*-
A, B, C, K = map(int, input().split())
W = np.array([[0,1,1], [1,0,1], [1,1,0]])
bef_X = np.array([A, B, C])
aft_X = np.dot(np.linalg.matrix_power(W, K),  bef_X)

ans = aft_X[0] - aft_X[1]

print("{0}".format(ans if ans <= 10**18 else 'unfair'))