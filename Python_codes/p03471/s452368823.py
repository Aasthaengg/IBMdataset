def resolve():
    N, Y = [int(i) for i in input().split()]
    for x in range((Y // 10000) + 1):
        for y in range((Y // 5000) + 1):
            z = N - x - y
            if z < 0:
                continue
            if 10000 * x + 5000 * y + 1000 * z == Y:
                print(x, y, z)
                return
    print(-1, -1, -1)

resolve()
