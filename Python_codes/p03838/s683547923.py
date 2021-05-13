x, y = map(int, input().split())
ax = abs(x)
ay = abs(y)
if ax == ay:
    print(int(x != y))
elif ax > ay:
    if y <= 0:
        if x > 0:
            print(1 + ax - ay)
        else:
            print(ax - ay)
    else:
        if x > 0:
            print(2 + ax - ay)
        else:
            print(1 + ax - ay)
else:
    if y > 0:
        if x >= 0:
            print(ay - ax)
        else:
            print(1 + ay - ax)
    else:
        if x >= 0:
            print(1 + ay - ax)
        else:
            print(2 + ay - ax)
