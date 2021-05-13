import sys
def gcm(a,b):
    if a%b==0: return b
    return gcm(b,a%b)

for s in sys.stdin:
    a,b=map(int,s.split())
    if a<b:a,b=b,a
    c=gcm(a,b)
    print c,a/c*b