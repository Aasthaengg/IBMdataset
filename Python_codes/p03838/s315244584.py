x,y = map(int,input().split())
if x*y >= 0:
    if x == 0:
        if y < 0:
            print(1-y)
        else:
            print(y)
    elif y == 0:
        if x > 0:
            print(1+x)
        else:
            print(-x)
    elif x > y:
        print(2+x-y)
    else:
        print(y-x)
else:
    if x >= -y:
        print(1+x+y)
    else:
        print(1-x-y)