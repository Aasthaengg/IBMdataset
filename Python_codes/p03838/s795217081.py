x, y = map(int, input().split())

if x <= y:
    if 0 <= x or y <= 0:
        print(y-x)
    elif abs(x) >= abs(y):
        print(abs(x) - abs(y) + 1)
    else:
        print(1+abs(y)-abs(x))
else:
    if 0 < y or x < 0:
        print(1+abs(x-y)+1)
    elif x == 0 or y == 0:
        print(abs(x-y)+1)
    elif abs(x) >= abs(y):
        print(1+abs(x)-abs(y))
    else:
        print(abs(y)-abs(x)+1)