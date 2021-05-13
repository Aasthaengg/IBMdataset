x, y = map(int, input().split())

if x <= y:
    if 0 <= x * y:
        print(y - x)
    else:
        print(abs(x + y) + 1)
else:
    if 0 < x * y:
        print(x - y + 2)
    elif x * y <= 0:
        print(abs(y + x) + 1)