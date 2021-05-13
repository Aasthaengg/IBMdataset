def resolve():
    W, a, b = list(map(int, input().split()))
    res = 0
    if a > b + W:
        res = a - (b + W)
    elif b > a + W:
        res = b - (a + W)
    print(res)



if '__main__' == __name__:
    resolve()