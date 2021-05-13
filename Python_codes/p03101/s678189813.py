import numpy as np

H, W = map(int, input().split())
h, w = map(int, input().split())
table = np.ones((H, W), dtype='int')
table[:h,:] = 0
table[:,:w] = 0
num = np.sum(table)
print(num)