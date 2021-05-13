import sys

def gcd(m,n):
    if n==0: return m
    return gcd(n,m%n)

for l in sys.stdin:
    a,b=map(int,l.split())
    d=gcd(a,b)
    print d,a/d*b