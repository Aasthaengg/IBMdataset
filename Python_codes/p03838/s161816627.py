x, y = map(int, input().split())
if x*y>=0:
    if x<y:
        print(y-x)
    else:
        print(x-y+2 if x*y>0 else x-y+1)
else:
    print(abs(abs(x)-abs(y))+1)