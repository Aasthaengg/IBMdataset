while True:
    (x, y) = (int(i) for i in input().split())
    if x == 0 and y == 0:
        break
    elif x <= y:
        print(x, y)
    else:
        print(y, x)