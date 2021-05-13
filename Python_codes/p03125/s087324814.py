def abc():
    a, b = map(int, input().rstrip().split())
    if b % a == 0:
        print(a + b)
    else:
        print(b -a)


abc()
