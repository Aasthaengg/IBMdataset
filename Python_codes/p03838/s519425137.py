x, y = map(int, input().split())
if x > 0:
    if y >= x:
        print(y - x)
    elif -x <= y and y <= 0:
        print(1 + x + y)
    elif 0 < y and y < x:
        print(x - y + 2)
    elif y < -x:
        print(-y - x + 1)
elif x == 0:
    if y >= 0:
        print(y)
    elif y < 0:
        print(-y + 1)
elif x < 0:
    if x <= y and y <= 0:
        print(y - x)
    elif 0 < y and y < -x:
        print(-y - x + 1)
    elif y >= -x:
        print(1 + x + y)
    elif y < x:
        print(x - y + 2)
