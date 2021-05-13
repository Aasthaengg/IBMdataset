def resolve():
    A, B = [int(x) for x in input().split(" ")]
    n = 0
    t = 1
    while t < B:
        t -= 1
        t += A
        n += 1
    print(n)
resolve()