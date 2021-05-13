import math
import sys
def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)
def lcm(a,b):
    return a/gcd(a,b)*b
for l in sys.stdin:
    a=list(map(int,l.split()))
    print("%d %d"%(gcd(a[0],a[1]),lcm(a[0],a[1])))
