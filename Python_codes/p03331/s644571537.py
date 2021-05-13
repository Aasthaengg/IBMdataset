N = int(input())


def f(x):
    ret = 0
    while x:
        x, r = divmod(x, 10)
        ret += r
    return ret


ret = 10 ** 9
for a in range(1, N):
    b = N - a
    ret = min(ret, f(a) + f(b))
print(ret)
