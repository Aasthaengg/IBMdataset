import numpy as np
from numba import jit
import random
verbose = False
rand = False

if rand:
    N, K = random.choice(range(10)), random.choice(range(10))
    A = np.array(random.choices(range(10**9), k=N))
else:
    N, K = list(map(int, input().split()))
    A = np.array(list(map(int, input().split())), dtype=np.int64)

ul = np.ceil(np.sum(A)/(K+1))
ll= np.floor(np.max(A)/(K+1))

EPS = 1 / 10**6

@jit(nopython=True)
def cut(A, c, N):
    return (np.sum(np.ceil(A/c))-N)

c = np.ceil((ul+ll)/2)
mx = np.max(A)
while True:
    if ul-ll <= 1:
        break
    nk = cut(A, c, N)
    if verbose:
        print('c:', c, 'nk:', nk, 'ul - ll:', ul, '/', ll)
    prev = c
    if nk  >K: # more cuts than target; larger logs can be made
        ll = c
        c = np.floor((ul + c)/2)
    else: #i.e. nk < K, less cuts than target
        ul = c
        c = np.ceil((c + ll)/2)
        
if cut(A, ll+EPS, N) >= K:
    print(np.min((np.max(A), int(ul))))
else:
    print(int(ll))
    
