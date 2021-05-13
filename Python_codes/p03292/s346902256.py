import numpy as np

a = list(map(int, input().split()))
def task(b):
    return abs(b[1] - b[0]) + abs(b[2] - b[1])
a = np.array(a)
p = np.array([[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]) - 1
Min = np.inf
for i in range(6):
    Min = min(Min, task(a[p[i,:]]))
print(Min)
