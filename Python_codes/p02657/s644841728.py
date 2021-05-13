import numpy as np
#from numba import njit

def getVar():
    return map(int, input().split())
def getArray():
    return np.array(list(map(int, input().split())))

(A, B) = getVar()

print(str(A*B))