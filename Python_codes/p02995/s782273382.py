import math
a,b,c,d = map(int,input().split())

ans = b-(a-1)

def lcm(x,y):
    return x * y // math.gcd(x,y)

ca = (a-1)//c
cb = b//c
da = (a-1)//d
db = b//d
cda = (a-1)//lcm(c,d)
cdb = b//lcm(c,d)
ans -= (cb+db-cdb) - (ca+da-cda)
print(ans)