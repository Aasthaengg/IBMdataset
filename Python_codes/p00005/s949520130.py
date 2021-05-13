import sys
def gcd(a,b):
    if (b == 0):
        return a
    return gcd(b,a%b)
for line in sys.stdin:
    a,b = [int(x) for x in line.split()]
    d = gcd(a,b)
    print d,a*b/d