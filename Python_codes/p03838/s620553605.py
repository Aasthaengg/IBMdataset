x, y = map(int, input().split())
if y == 0 and x <= 0:
    print(abs(x-y))
elif x >= 0 and y == 0:
    print(abs(x-y)+1)
elif x >= 0 and y >= 0:
    if x <= y:
        print(abs(x-y))
    else:
        print(abs(x-y)+2)
elif x <= 0 and y >= 0:
    print(abs(y-abs(x))+1)
elif x >= 0 and y <= 0:
    print(abs(x-abs(y))+1)
elif x <= y:
    print(abs(x-y))
else:
    print(abs(x-y)+2)