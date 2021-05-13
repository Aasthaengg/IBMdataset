x, y = map(int, input().split())

if 0 <= x and 0 <= y:
    if x <= y:
        res = abs(x - y)
    elif y == 0:
        res = abs(x - y) + 1
    else:
        res = abs(x - y) + 2
elif x < 0 and y <= 0:
    if x <= y:
        res = abs(x - y)
    else:
        res = abs(x - y) + 2
else:
    res = abs(abs(x) - abs(y)) + 1

print(res)
