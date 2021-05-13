import numpy as np
N = int(input())
l = np.array(list(map(int,input().split())))
ans = 'Yes'
M = l[0]

for i in range(1,N):
    if l[i] > l[i-1]:
        M = l[i]

    if l[i]< M-1:
        ans ='No'
        break
print(ans)