import numpy as np
N, M = map(int, input().split())

A = np.zeros((N,M))
for i in range(N):
    a = list(map(int, input().split()))
    a = a[1:]
    A[i, 0:len(a)] = a

for i in range(N):
    a = A[i]
    a = a[(a != 0) & (a <= M)]
    if i == 0:
        s = set(list(a))
    else:
        _s = set(list(a))
        s &= _s

print(len(s))