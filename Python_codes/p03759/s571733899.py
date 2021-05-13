def abc():
    a, b, c = map(int, input().rstrip().split())
    print('YES' if (b - a) == (c - b) else 'NO')


abc()
