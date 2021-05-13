input()
from collections import *
c=Counter(map(int,input().split()))
f=lambda x:sorted(-k for k,v in c.items() if v>x)
a=0;r=f(1);s=f(3)
if len(r)>1: a=r[0]*r[1]
if s: a=max(a,s[0]**2)
print(a)