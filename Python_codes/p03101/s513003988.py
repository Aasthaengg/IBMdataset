H,W = map(int,input().split())
r,c = map(int,input().split())

import numpy as np

matrix = np.ones((H,W),dtype="uint8")
matrix[0:r,:] = 0
matrix[:,0:c] = 0
print(matrix.sum())
