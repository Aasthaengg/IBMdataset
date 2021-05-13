import math
a,b,c,d = map(int,input().split())
e = math.floor(c*d / math.gcd(c,d))

def div(z):
    p = (z//c) + (z//d) - (z//e)
    return p

x = a-1 - div(a-1)
y = b - div(b)
print(y-x)