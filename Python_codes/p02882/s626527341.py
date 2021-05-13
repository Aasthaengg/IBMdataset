def binary_search(ok, ng, error, test):
    """
    :param ok: solve(x) = True を必ず満たす点
    :param ng: solve(x) = False を必ず満たす点
    """
    while abs(ok - ng) > error:
        mid = (ok + ng) / 2
        if test(mid):
            ok = mid
        else:
            ng = mid
    return ok

def max2(x,y):
    return x if x > y else y

def min2(x,y):
    return x if x < y else y

def test(y):
    return (a**3*tan(y)/2 + (b-a*tan(y))*cos(y)*a**2/cos(y) if b-a*tan(y) >= 0 else b**2*a*tan(pi/2-y)/2 ) >= x

from math import *
a, b, x = map(int, input().split())


print(binary_search(0,pi/2,10**(-8), test)*180/pi)






