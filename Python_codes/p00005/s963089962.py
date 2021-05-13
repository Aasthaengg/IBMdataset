import sys
def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b/gcd(a,b)
for i in sys.stdin.readlines():
    a,b=map(int,i.split())
    print "{} {}".format(gcd(a,b),lcm(a,b))