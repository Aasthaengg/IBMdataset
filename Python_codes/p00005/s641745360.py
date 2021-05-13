import sys
def g(a,b):
    if b==0: return a
    return g(b,a%b)
for l in sys.stdin:
    a,b=map(int,l.split())
    c=g(a,b)
    print c,a/c*b