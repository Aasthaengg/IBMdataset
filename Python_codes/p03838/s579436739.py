x, y = map(int, input().split())

if x*y < 0:
    print(abs(abs(x)-abs(y))+1)
elif x*y == 0:
    if x < y:
        print(y-x)
    else:
        print(x-y+1)
else:
    if x < y:
        print(y-x)
    else:
        print(x-y+2)
