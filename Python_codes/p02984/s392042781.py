import numpy as np


n = int(input())
r = np.array(list(map(int,input().split())))

pm = np.array([1,-1] * (n//2) + [1])


d = []
tmp = sum(r * pm)
d.append(str(tmp))
tmp -= r[0]

for i in range(n-1):
    tmp = r[i] - tmp
    d.append(str(tmp))
    tmp -= r[i+1]

print(' '.join(d))