import sys
import math
a=sys.stdin.readline()
res=[i for i in a.split()]
r1,r2=float(res[0]),float(res[1])
v1,v2=r1.is_integer(),r2.is_integer()
if v1==v2==True:
    N,D=int(r1),int(r2)
    if 1<=(N and D)<=20:
        w=2*D+1
        print(int(math.ceil(N/w)))