import sys
a=sys.stdin.readline()
res=[i for i in a.split()]
A,B,C=[float(res[i]) for i in (0,1,2)]
E,F,G=A.is_integer(),B.is_integer(),C.is_integer()
if E==F==G==True:
    if 1<=B<=A<=20 and 1<=C<=20:
        w=C-A+B
        if w<0:
            print(0)
        else:
            print(int(w))