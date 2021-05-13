#from random import randint

def f(h,w,m,ins):
    yp = [0]*h
    xp = [0]*w
    s = set()
    for hi,wi in ins:
        s.add((hi-1,wi-1))
        yp[hi-1] += 1
        xp[wi-1] += 1
    ypm = max(yp)
    xpm = max(xp)
    yps = [i for i in range(h) if yp[i] == ypm]
    xps = [i for i in range(w) if xp[i] == xpm]
    ans = ypm+xpm
    for ypsi in yps:
        for xpsi in xps:
            if not (ypsi,xpsi) in s:
                return ans
    return ans-1

if __name__ == "__main__":
    if False:
        while True:
            h,w = randint(1,10**5*3),randint(10**5,10**5*3)
            m = randint(1,min(h*w,10**5*3))
            ins = [(randint(1,h),randint(1,w)) for i in range(m)]
            ans = f(h,w,m,ins)
            print(ans)
    else:
        h,w,m = map(int,input().split())
        ans = f(h,w,m,[list(map(int,input().split())) for i in range(m)])
        print(ans)
