# AGC008A

def func(x, y):
    if y >= x:
        if x >= 0:
            return y - x
        else:
            if y > 0:
                if abs(x) > abs(y):
                    return 1 - x - y
                else:
                    return 1 + x + y
            elif y <= 0:
                return y - x
    else:
        if x >= 0:
            if y < 0:
                if abs(x) > abs(y):
                    return 1 + x + y
                else:
                    return 1 - x - y
            elif y == 0 or y == 1:
                return x + 1
            else:
                if abs(x) > abs(y):
                    return 1 + x + y
                else:
                    return 1 + y - x
        else:
            return 2 + x - y

x, y = map(int, input().split())
print(func(x, y))
