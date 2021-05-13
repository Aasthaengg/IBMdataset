import numpy as np
from numba import njit
 
@njit(cache=True)
def main(N, s):
    dpt = np.zeros((N+1, N+1), dtype=np.int16)
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if s[j-1] == s[i-1]:
                if j - dpt[i-1][j-1] > i:
                    dpt[i][j] = dpt[i-1][j-1] + 1
 
    return np.amax(dpt)
 
if __name__ == '__main__':
    N = int(input())
    s = np.array([ord(c) for c in input()]) 
 
    print(main(N, s))