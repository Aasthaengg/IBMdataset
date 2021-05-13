def solver(x, y):
    ans1 = abs(x) + abs(y)
    ans2 = abs(abs(x) - abs(y))
    res = 0
    if x < y:
        if x * y >= 0:
            res = ans2
        else:
            res = 1 + ans2
    else:
        if 0 < y:
            res = 2 + ans2
        elif x * y <= 0:
            res = 1 + ans2
        else:
            if abs(x) <= abs(y):
                res = 2 + ans2
            else:
                res = 1 + ans1
    return res

x, y = map(int, input().split())
print(solver(x, y))