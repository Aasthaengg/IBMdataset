x,y=map(int,input().split())
if abs(x) == abs(y):
    print(1)
elif x==0:
    if y < 0:
        print(1+abs(y))
    else:
        print(abs(y))
elif x > 0:
    if abs(y) < x:
        if y == 0:
            print(1+y+x)
        elif y>0:
            print(abs(abs(y)-abs(x))+2)
        else:
            print(y+x+1)
    else:
        if y > 0:
            print(y-x)
        else:
            print(abs(y)-x+1)
else:
    if abs(y) <abs(x):
        if y >0 :
            print(1+abs(abs(x)-abs(y)))
        elif y==0:
            print(abs(x))
        else:
            print(abs(-x+y))
    else:
        if y >0:
            print(1+y+x)
        else:
            print(2+x-y)
