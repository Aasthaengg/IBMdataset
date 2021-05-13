import numpy as np
#from numba import njit

#(N, K) = map(int, input().split())
#A = np.array(list(map(int, input().split())))
N = int(input())
h = np.array(list(map(int, input().split())))

#@njit

def solve(N,h):
    s = 0
    while (np.any(h > 0)):
        w = np.where(h > 0)[0]
        l = w[0]
        r = w[0]
        i = 1
        while (i < len(w)):
            if (w[i] == r + 1):
                r = w[i]
            i += 1
        
        h = np.concatenate([h[:l], h[l:r+1]-1, h[r+1:]])
        s += 1
    return s

print(solve(N,h))
