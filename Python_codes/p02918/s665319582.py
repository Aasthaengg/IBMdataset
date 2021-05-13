n,k=map(int,input().split())
s=input()
from itertools import groupby as gb
var=[len(list(b)) for a,b in gb(s)]
ans=n-len(var)
G=len(var)
if s[0]==s[-1]:
    t=G//2
    h=G-G//2+2
else:
    t,h=G-G//2,G//2+2
#print(f"{t=},{h=},{k=},{ans=},")
if k>min(t,h):
    print(n-1)
elif k==min(t,h):
    print(n-1)
else:
    print(ans+2*k)