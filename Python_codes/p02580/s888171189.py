from random import randint
import numpy as np
from numba import njit


#@njit
def f(h,w,m,ins):
    yp = np.zeros((h,2),dtype=np.int)
    xp = np.zeros((w,2),dtype=np.int)
    yp[:,1] = np.arange(h)
    xp[:,1] = np.arange(w)
    ans = 0
    s = set()
    for hi,wi in ins:
        s.add((hi-1,wi-1))
        yp[hi-1,0] += 1
        xp[wi-1,0] += 1
    ypm = yp[:,0].max()
    xpm = xp[:,0].max()
    yps = yp[yp[:,0] == ypm][:,1]
    xps = xp[xp[:,0] == xpm][:,1]
    #y = yp[yps]
    for ypsi in yps:
        for xpsi in xps:
            a = yp[ypsi,0]+xp[xpsi,0]
            if (ypsi,xpsi) in s:
                a -= 1
                ans = max(ans,a)
            else:
                return a
    return ans


if False:
    while True:
        h,w = randint(1,10**5*3),randint(1,10**5*3)
        m = randint(1,min(h*w,10**5*3))
        ins = [(randint(1,h),randint(1,w)) for i in range(m)]
        ans1 = f1(h,w,m,ins)
        ans2 = f2(h,w,m,ins)
        if ans1 != ans2:
            print("!!!!")
            print(h,w,m)
            print(ins)
else:
    h,w,m = map(int,input().split())
    ans = f(h,w,m,[tuple(map(int,input().split())) for i in range(m)])
    print(ans)
