while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        for _ in range(a):
            x = '#' * b
            print(x)
        print()
