import numpy as np
N,M,Q = (int(x) for x in input().split())
route = np.zeros((N,N))
for i in range(M):
    L,R = (int(x) for x in input().split())
    route[L-1][R-1] += 1
cs1 = np.cumsum(route,axis=1)
cs2 = np.cumsum(cs1,axis=0)
for i in range(Q):
    p,q = (int(x) for x in input().split())
    if p == 1:
        print(int(cs2[q-1][q-1]))
    else:
        print(int(cs2[q-1][q-1]-cs2[p-2][q-1]))