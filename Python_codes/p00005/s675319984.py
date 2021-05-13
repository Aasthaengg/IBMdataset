import sys

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

for line in sys.stdin:
    (a,b)=line.split(" ")
    a=eval(a)
    b=eval(b)
    g=gcd(a,b)
    print("%d %d" % (g,a*b/g))