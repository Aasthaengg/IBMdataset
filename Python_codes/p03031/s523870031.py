import numpy as np
 
N, M = map(int, input().split())
array = np.zeros([M, N])
for i in range(M):
    l = list(map(int, input().split()))
    for j in l[1:]:
        array[i, j-1] = 1
p = np.array(list(map(int, input().split())))
count = 0
for i in range(1<<N):
    array_i = array.copy()
    for j in range(N):
        if i&(1<<j):
            array_i[:, j-1] = 0
    if sum(array_i.sum(1)%2 == p)==M:
        count += 1
print(count)