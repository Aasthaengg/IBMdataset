x,y = map(int,input().split())
if x > y:
    if x < 0 and y < 0:
        print(abs(abs(y)-abs(x))+2)
    if x >= 0 and y < 0:
        print(abs(abs(y)-abs(x))+1)
    if x >= 0 and y >= 0:
        if y == 0:
            print(abs(abs(y)-abs(x))+1)
        else:
            print(abs(abs(y)-abs(x))+2)
elif x < y:
    if x < 0 and y < 0:
        print(abs(abs(y)-abs(x)))
    if x < 0 and y >= 0:
        if y == 0:
            print(abs(abs(y)-abs(x)))
        else:
            print(abs(abs(y)-abs(x))+1)
    if x >= 0 and y >= 0:
        print(abs(abs(y)-abs(x)))