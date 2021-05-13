from random import randint
import numpy as np
from numba import njit


@njit(cache=True)
def f(h,w,m,yp,xp,s):
    ypm = yp[:,0].max()
    xpm = xp[:,0].max()
    yps = yp[yp[:,0] == ypm][:,1]
    xps = xp[xp[:,0] == xpm][:,1]
    ans = 0
    for ypsi in yps:
        for xpsi in xps:
            a = yp[ypsi,0]+xp[xpsi,0]
            if (ypsi,xpsi) in s:
                a -= 1
                ans = max(ans,a)
            else:
                return a
    return ans


h,w,m = map(int,input().split())
s = set()
yp = np.zeros((h,2),dtype=np.int)
xp = np.zeros((w,2),dtype=np.int)
yp[:,1] = np.arange(h)
xp[:,1] = np.arange(w)
for i in range(m):
    hi,wi = map(int,input().split())
    s.add((hi-1,wi-1))
    yp[hi-1,0] += 1
    xp[wi-1,0] += 1
ans = f(h,w,m,yp,xp,s)
print(ans)
