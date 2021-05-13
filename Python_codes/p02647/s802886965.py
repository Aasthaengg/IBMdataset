import sys
import numpy as np
from numba import jit
 
readline = sys.stdin.readline
 
@jit
def loop(n,k,a):
    for j in range(k):
        b = np.zeros(n+1, dtype=np.int64)
        for i in range(n):
            b[max(i-a[i], 0)] += 1
            b[min(i+a[i]+1, n)] -= 1
        a = np.cumsum(b)[:-1]
        if np.all(a==n):
            return(a)
            break
    else:
        return(a)
 
 
n, k = map(int, readline().split())
a = np.array(readline().split(), dtype=np.int64)
 
ans = loop(n,k,a)
print(*ans)