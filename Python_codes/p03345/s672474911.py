def resolve():
    a, b, c, k = [int(i) for i in input().split()]
    if k % 2 == 0:
        print(a - b)
    else:
        print((a - b) * -1)


resolve()
