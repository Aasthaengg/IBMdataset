def ninebank(val):
    left = val
    ret = 0
    div = 9 ** 5
    while div > 0:
        ret += left // div
        left = left % div
        div = div // 9
    return ret


def sixbank(val):
    left = val
    ret = 0
    div = 6 ** 10
    while div > 0:
        ret += left // div
        left = left % div
        div = div // 6
    return ret


n = int(input())
ret = 10 ** 10
for i in range(n+1):
    x = ninebank(i)
    y = sixbank(n - i)
    ret = min(ret, x + y)
print(ret)
