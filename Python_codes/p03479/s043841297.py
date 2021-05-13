def resolve():
    x, y = map(int, input().split())
    a = []

    d = y // x

    i = 0
    while 2 ** i <= d:
        i += 1

    print(i)

resolve()