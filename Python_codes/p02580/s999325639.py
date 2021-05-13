#from random import randint
import numpy as np


#@njit
def f(h,w,m,ins):
    yp = np.zeros(h,dtype=np.int)
    xp = np.zeros(w,dtype=np.int)
    #yp[:,1] = np.arange(h)
    #xp[:,1] = np.arange(w)
    ans = 0
    s = set()
    for hi,wi in ins:
        s.add((hi-1,wi-1))
        yp[hi-1] += 1
        xp[wi-1] += 1
    ypm = yp[yp.argmax()]
    xpm = xp[xp.argmax()]
    yps = np.where(yp == ypm)[0].tolist()
    xps = np.where(xp == xpm)[0].tolist()
    #y = yp[yps]
    for ypsi in yps:
        for xpsi in xps:
            a = yp[ypsi]+xp[xpsi]
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
        ans = f(h,w,m,ins)
        print(ans)
else:
    h,w,m = map(int,input().split())
    ans = f(h,w,m,[tuple(map(int,input().split())) for i in range(m)])
    print(ans)
