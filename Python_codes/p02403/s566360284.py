while True:
    h, w = map(int, input().split())
    if h == 0:
        exit()
    [print("#" * w) for i in range(h)]
    print()