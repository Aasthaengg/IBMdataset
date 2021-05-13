import numpy as np
N,M = (int(X) for X in input().split())
Shop = np.zeros((N,2),dtype=int)
for T in range(0,N):
    Shop[T,:] = (np.array([int(X) for X in input().split()]))
Shop = Shop[np.argsort(Shop[:,0])]
Rest = M
Pric = 0
for T in range(0,N):
    Pric += Shop[T,0]*Shop[T,1]
    Rest -= Shop[T,1]
    if Rest<0:
        Pric += Rest*Shop[T,0]
        break
print(Pric)