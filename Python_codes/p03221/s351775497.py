import numpy as np
#from numba import njit

#(N, K) = map(int, input().split())
#A = np.array(list(map(int, input().split())))
(N,M) = map(int, input().split())
PY = []

for i in range(1,M+1):
    (P,Y) = map(int, input().split())
    PY += (i,P,Y),

sorter = lambda x: (x[1], x[2], x[0])
PY = sorted(PY, key=sorter)

result = {}

order = 1
last = 0
for (i, P, Y) in PY:
    if last != P:
        order = 1
        last = P
    result.update({i:('{:0>6}'.format(P) + '{:0>6}'.format(order))})
    order += 1

for i in range(1,M+1):
    print(result[i])
