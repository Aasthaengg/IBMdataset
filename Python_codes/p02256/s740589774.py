x, y = map(int, input().split())
while True:
    if x > y:
        x = x % y
        if x == 0:
            print(y)
            break
    else:
        y = y % x
        if y == 0:
            print(x)
            break
