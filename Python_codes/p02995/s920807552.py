import math
def yaku(n,p,q):
    lcm = (p*q)//math.gcd(p,q)
    return (n//p + n//q - n//lcm)
a,b,c,d = map(int,input().split())
print((b-a+1)-((yaku(b,c,d)) - yaku(a-1,c,d)))