x,y=map(int,input().split())
if x==0 or y==0:
    if y>=x:
        print(abs(y-x))
    else:
        print(abs(y-x)+1)
else:
    if x>0 and y>0:
        if y>=x:
            print(abs(y-x))
        else:
            print(abs(y-x)+2)
    if x<0 and y<0:
        if y>=x:
            print(abs(y-x))
        else:
            print(abs(y-x)+2)
    elif x>0 and y<0:
        print(abs(-y-x)+1)
    elif x<0 and y>0:
        print(abs(y+x)+1)