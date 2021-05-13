N,A,B = map(int, input().split())
hs = [int(input()) for _ in range(N)]

def f(x):
    """
    xが少ないとfalse
    xが大きいとtrue
    """
    As = [max(0,h-B*x) for h in hs]
    Bs = [-(-a//(A-B)) for a in As]
    
    return sum(Bs) <= x


def  binarySearch(l,r):
    while r - l > 1:
        mid = (l+r)//2
        if f(mid):
            r = mid
        else:
            l = mid
    return r


r = 10**9+1
print(binarySearch(0,r))