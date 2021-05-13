import sys
import numpy as np
import itertools

[N,M] = input().split()
N = int(N)
M = int(M)
a =[]
p = []
list_bin = []

for j in range(M):
    list_temp = [int(s) for s in input().split()]
    list_temp.pop(0)
    for i in range(N):
        if i+1 in list_temp:
            list_bin.append(1)
        else:
            list_bin.append(0)

    a.append(list_bin)
    list_bin = []
p = [int(s) for s in input().split()]

arr_switch = np.array(a)
arr_p = np.array(p)
arr_pattern = np.array(list(itertools.product([0,1], repeat=N)))

count = 0
flag = 1
for switch in arr_pattern:
    for m in range(M):
        if (not (np.dot(switch, arr_switch[m]) % 2 == arr_p[m])) or  (np.dot(switch, np.ones(N)) == -1):
           flag = 0
    if flag == 1:
        count = count + 1
    flag=1
print(count)
