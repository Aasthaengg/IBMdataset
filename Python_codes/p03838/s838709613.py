x, y = map(int, input().split())
dif = abs(abs(x) - abs(y))
if x < 0 and y < 0:
    if x < y:
        print(dif)
        exit()
    else:
        print(dif+2)
        exit()
if x >= 0 and y >= 0:
    if x > y:
        if y == 0:
            print(dif+1)
            exit()
        print(dif+2)
        exit()
    else:
        print(dif)
        exit()
if x >= 0:
    print(dif+1)
else:
    if y == 0:
        print(dif)
    else:
        print(dif+1)
