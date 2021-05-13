# AGC008 A Simple Calculator

x, y = map(int, input().split())
_x = abs(x)
_y = abs(y)

if x > 0 and y > 0:
    if x <= y:
        print(y-x)
    else:
        print(x-y+2)
elif x * y < 0:
    print(abs(_y-_x)+1)
elif x == 0:
    if y >= 0:
        print(y)
    else:
        print(_y+1)
elif y == 0:
    if x > 0:
        print(x+1)
    else:
        print(_x)
else:
    if _x < _y:
        print(_y-_x+2)
    else:
        print(_x-_y)