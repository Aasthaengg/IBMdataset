x, y = map(int, input().split())
if abs(y) > abs(x):
    if (x >= 0 and y > 0):
        print(abs(y - x))
    elif x * y <= 0:
        print(abs(y) - abs(x) + 1)
    else:
        print(abs(y) - abs(x) + 2)
else:
    if x > 0 and y > 0:
        print(x - y + 2)
    elif x * y < 0 or (y == 0 and x > 0):
        print(abs(x) - abs(y) + 1)
    else:
        print(abs(x - y))