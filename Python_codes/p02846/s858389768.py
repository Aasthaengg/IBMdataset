t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
d = a1*t1+a2*t2-b1*t1-b2*t2
de = -a1*t1+b1*t1
if d == 0:
    print('infinity')
else:
    if a1<b1:
        if d < 0:
            print(0)
        else:
            if de%d == 0:
                print(2*(de//d))
            else:
                print(2*(de//d)+1)
    else:
        if d > 0:
            print(0)
        else:
            de = -de
            d = -d
            if de%d == 0:
                print(2*(de//d))
            else:
                print(2*(de//d)+1)

