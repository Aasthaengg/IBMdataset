import sys
def gcm(a,b):
    x=gcm(b,a%b) if b else a
    return x
for s in sys.stdin:
    a,b=map(int,s.split())
    c=gcm(a,b)
    print c,a/c*b