x,y = map(int,input().split())
if y == x:
    print(0)
elif y == 0:
    if x > 0:
        print(x+1)
    else:
        print(-x)
else:
    if abs(y) >= abs(x):
        tmp = abs(y)-abs(x)
        if x>=0 and y>=0:
            print(tmp)
        elif x>=0 and y<0:
            print(tmp+1)
        elif x<0 and y>=0:
            print(tmp+1)
        else:
            print(tmp+2)
    else:
        if x>=0 and y>=0:
            print(-y+x+2)
        elif x>=0 and y<0:
            print(x+y+1)
        elif x<0 and y>=0:
            print(-y-x+1)
        else:
            print(y-x)