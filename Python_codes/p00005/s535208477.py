import sys

def gcd(x,y):
    if(y>0):
        return gcd(y,x%y)
    else:
        return x

def lcm(x,y):
    return x/gcd(x,y)*y

for x in sys.stdin.readlines():
    n = [float(y) for y in x.split()]

    print "%d %d" % (gcd(n[0], n[1]),(lcm(n[0], n[1])))