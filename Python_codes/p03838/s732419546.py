x, y = map(int, input().split())
ax, ay = abs(x), abs(y)


def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1


if x == 0 or y == 0:
    print(abs(x-y)+(x > y))
else:
    if sign(x) != sign(y):
        print(abs(ax - ay) + 1)
    else:
        if x < y:
            print(y - x)
        else:
            print(abs(ax - ay) + 2)
