x,y = map(int,input().split())
if y == x:
    print(0)
elif abs(y) == abs(x):
    print(1)
elif x*y > 0:
    if x < y:
        print(y-x)
    else:
        print(x-y+2)
elif x*y == 0:
    if x < y:
        print(y-x)
    else:
        print(x-y+1)
else:
    if x < y:
        print(min(y-x,abs(abs(x)-abs(y))+1))
    else:
        print(min(x-y,abs(abs(x)-abs(y))+1))
