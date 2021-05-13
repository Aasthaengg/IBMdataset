import sys
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b,gcdnum=0):
    if gcdnum==0:
        return a * b // gcd (a, b)
    else:
        return a * b // gcdnum

for line in sys.stdin:
    a,b = map(int,line.split())
    gcdnum = gcd(a,b)
    print "%d %d"%(gcdnum,lcm(a,b,gcdnum))