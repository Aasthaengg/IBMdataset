def abc():
    x, y = map(int, input().rstrip().split())
    if x % y == 0:
        print(-1)
        return
    print(x)


abc()
