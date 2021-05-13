import sys

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

for ab in sys.stdin:
    a,b=map(int,ab.split(" "))
    if a<=b:
        tmp = a
        a = b
        b = tmp
    g = gcd(a,b)
    l = a*b/g
    print g,l