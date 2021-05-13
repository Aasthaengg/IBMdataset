a, b = map(int, input().split())

if a == 1:
    if b == 1:
        print(1000000)
    elif b == 2:
        print(500000)
    elif b == 3:
        print(400000)
    else:
        print(300000)
elif a == 2:
    if b == 1:
        print(500000)
    elif b == 2:
        print(400000)
    elif b == 3:
        print(300000)
    else:
        print(200000)
elif a == 3:
    if b == 1:
        print(400000)
    elif b == 2:
        print(300000)
    elif b == 3:
        print(200000)
    else:
        print(100000)
elif a >= 3:
    if b == 1:
        print(300000)
    elif b == 2:
        print(200000)
    elif b == 3:
        print(100000)
    else:
        print(0)