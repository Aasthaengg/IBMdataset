x,y = map(int,input().split())
if (x+y)>=23:
    print((x+y)%24)
else:
    print(x+y)
