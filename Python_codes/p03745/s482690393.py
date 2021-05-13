import sys
N=int(sys.stdin.readline().strip())
A=map(int, sys.stdin.readline().split())
ans=0
trend=None
prev=None
for a in A:
    if prev is None:
        ans+=1
    elif prev<a:
        if trend is None:
            trend="plus"
        elif trend=="plus":
            pass
        elif trend=="minus":
            ans+=1
            trend=None
    elif prev>a:
        if trend is None:
            trend="minus"
        elif trend=="plus":
            ans+=1
            trend=None
        elif trend=="minus":
            pass
    elif prev==a:
        if trend is None:
            pass
        elif trend=="plus":
            pass
        elif trend=="minus":
            pass
    prev=a

print ans