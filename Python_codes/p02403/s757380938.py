while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break

    for y in range(1, h + 1):
        for x in range(1, w + 1):
            print('#', end='')
        print('')
    print('')