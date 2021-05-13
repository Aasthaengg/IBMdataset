x,y = [int(x) for x in input().split()]

if x >= 0 and y >= 0 and x <= y:
    print(y-x)
elif x >= 0 and y >= 0 and y < x:
    if y != 0:
        print(x-y+2)
    else:
        print(x-y+1)
elif x < 0 and y < 0 and y < x:
    print(x-y+2)
elif x < 0 and y < 0 and x < y:
    print(y-x)
elif x >= 0 and y < 0:
    print(abs(abs(y)-x)+1)
elif x < 0 and y >= 0:
    print(min(abs(abs(x)-y)+1, y-x))