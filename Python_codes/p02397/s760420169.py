while True:
    x, y = sorted([int(i) for i in input().split()])
    if x == y == 0:
        break
    print(x, y)