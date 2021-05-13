# coding: utf-8
import numpy as np
from functools import lru_cache
import time

def main(): 
    if True:
        N = int(input())
    else:
        pass

    T = np.asarray([False]*(N**2))
    T = T.reshape(N,N)
    Res = np.copy(T)
    range_N = np.asarray(range(N))
    #range_N += 1

    if N % 2 == 0:
        for i,j in zip(range_N,range_N[::-1]):
            if i >= j: break
            T[i,j] = True
            T[j,i] = True
    else:
        for i,j in zip(range_N,range_N[::-1]):
            j -= 1
            if i >= j: break
            T[i,j] = True
            T[j,i] = True

    Res[T==True] = False
    Res[T==False] = True
    
    for i in range_N:
        Res[i,i] = False

    #print(Res)
    print(Res[Res].size//2)

    for i in range_N:
        for j in range_N[i:]:
            if Res[i,j] == True: print(i+1,j+1)
if __name__ =='__main__':
    main()