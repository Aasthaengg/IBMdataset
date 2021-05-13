x, y = map(int, input().split())
a = abs(abs(x) - abs(y))
if y == 0:
    if x < 0:
        print(a)
    else:
        print(a + 1)
elif x == 0:
    if y < 0:
        print(a + 1)
    else:
        print(a)
elif abs(x) < abs(y):
    if x > -1 and y > -1:
        print(a)
    elif x < 0 and y < 0:
        print(a + 2)
    else:
        print(a + 1)
else:
    if x > -1 and y > -1:
        print(a + 2)
    elif x < 0 and y < 0:
        print(a)
    else:
        print(a + 1)
