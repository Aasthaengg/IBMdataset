from functools import reduce

def mycmb(n,r,p):
    r = min(r,n-r)
    if r == 0:
        return 1
    over = reduce(lambda x,y:x*y%p,range(n,n-r,-1))
    under = reduce(lambda x,y:x*y%p,range(1,r+1))
    return (over * pow(under,p-2,p))%p


mod = 10**9+7

x,y = map(int, input().split())
n = (2*x-y) // 3
m = (2*y-x) //3

if (x+y) % 3 != 0:
    print(0)
    exit()

if n < 0 or m < 0:
    print(0)
    exit()

print(mycmb(n+m,n,mod))