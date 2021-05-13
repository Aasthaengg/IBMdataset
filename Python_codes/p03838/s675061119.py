x, y = map(int, input().split())


def f1(x, y):
    if y >= x:
        return y - x
    else:
        return 10**10


def f2(x, y):
    if -y >= x:
        return -y - x + 1
    else:
        return 10**10


def f3(x, y):
    if y >= -x:
        return y + x + 1
    else:
        return 10**10


def f4(x, y):
    if -y >= -x:
        return -y + x + 2
    else:
        return 10**10


ans = min(f1(x, y), f2(x, y), f3(x, y), f4(x, y))
print(ans)
