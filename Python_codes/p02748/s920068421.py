def resolve():
    A, B, M = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    zyc = [list(map(int, input().split())) for _ in range(M)]

    minAB = min(a) + min(b)
    for z, y, c in zyc:
        tmp = a[z - 1] + b[y - 1] - c
        minAB = min(minAB, tmp)
    print(minAB)


resolve()
