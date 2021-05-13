while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break

    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if y == 1 or y == h:
                print('#', end='')
            else:
                if x == 1 or x == w:
                    print('#', end='')
                else:
                    print('.', end='')
        print('')
    print('')