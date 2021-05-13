while True:
    x, y = [int(i) for i in input().split()]
    
    if x == y == 0:
        break

    if x > y:
        x, y = y, x

    print(x, y)