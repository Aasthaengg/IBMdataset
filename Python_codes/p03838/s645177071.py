x, y = map(int, input().split())

if x >= 0:
    if y >= x:
        print(y - x)
    elif y > 0:
        print(1 + x - y + 1)
    elif abs(y) < x:
        print(1 + x + y)
    else:
        print(1 + abs(x + y))
else:
    if y >= abs(x):
        print(1 + y + x)
    elif y > 0:
        print(abs(x + y) + 1)

    elif abs(y) <= abs(x):
        print(abs(y - x))
    else:
        print(1 + abs(y - x) + 1)