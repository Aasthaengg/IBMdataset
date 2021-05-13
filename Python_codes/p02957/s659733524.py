import sys
a=sys.stdin.readline()
res=[i for i in a.split()]
r1,r2=float(res[0]),float(res[1])
v1,v2=r1.is_integer(),r2.is_integer()
if v1==v2==True:
    A,B=int(r1),int(r2)
    if 0<=(A and B)<=1000000000:
        w=(A+B)/2
        v3=w.is_integer()
        if v3==True:
            print(int(w))
        elif v3!=True:
            print("IMPOSSIBLE")