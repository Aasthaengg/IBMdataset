x, y = input().split()
x = int(x)
y = int(y)
r = 1
while r > 0:
    if x >= y:
        r = x % y
    else:
        r = y % x

    if r != 0:
        x = y
        y = r
    else:
        print(y)