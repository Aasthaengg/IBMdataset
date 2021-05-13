def abc():
    a, b, c = map(int, input().rstrip().split())

    print('Yes' if a + b >= c else 'No')


abc()
