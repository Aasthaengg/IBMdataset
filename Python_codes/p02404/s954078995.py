while True:
    H, W = map(int, raw_input().split())
    if H == 0 or W == 0:
        break
    print '#' * W
    for _ in range(1, H - 1):
        print '#' + '.' * (W - 2) + '#'
    print '#' * W
    print ''