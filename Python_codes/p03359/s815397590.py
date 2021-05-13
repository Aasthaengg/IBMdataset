def abc():
    a, b = map(int, input().rstrip().split())
    if a <= b:
        print(a)
    else:
        print(a - 1)


abc()
