import numpy as np
import sys
sys.setrecursionlimit(500000)


N = int(input())
a = np.array([int(input()) for i in range(N)])


#回数i,インデックスn
def button(i,n):
    n_new = a[n-1]
    
    if i == N:
        if n != 2:
            print(-1)
            return
    if n_new == 2:
        print(i)
        return 
    else:
        return button(i+1,n_new)

button(1,1)