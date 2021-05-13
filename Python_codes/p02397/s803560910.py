x,y=input().split()
while (x!='0'or y!='0'):
    if(int(x)>int(y)):print("{} {}".format(y,x))
    else:print("{} {}".format(x,y))
    x,y=input().split()