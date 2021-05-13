import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))
data = []
if np.sum(a >= 0) == n:
    flag = 1
elif np.sum(a >= 0) == 0:
    flag = -1
else:
    max_a = np.max(a)
    max_ind = np.argmax(a)
    min_a = np.min(a)
    min_ind = np.argmin(a)
    if np.abs(max_a) > np.abs(min_a):
        flag = 1
        a = a + max_a
        for i in range(n):
            data.append([max_ind+1, i+1])
    else:
        flag = -1
        a = a + min_a
        for i in range(n):
            data.append([min_ind+1, i+1])
if flag == 1:
    for i in range(n-1):
        data.append([i+1, i+2])
else:
    for i in range(n-1, 0, -1):
        data.append([i+1, i])
print (len(data))
for i in range(len(data)):
    print (data[i][0], data[i][1])
