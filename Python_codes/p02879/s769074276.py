a1=input()
a2=[i for i in a1.split()]
x,y=float(a2[0]),float(a2[1])
v,v1=x.is_integer(),y.is_integer()
if 1<=x<=20 and 1<=y<=20 and v==v1==True:
    if 1<=x<=9 and 1<=y<=9:
        print(int(x*y))
    else:
        print('-1')