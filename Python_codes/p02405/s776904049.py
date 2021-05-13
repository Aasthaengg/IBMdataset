while True:
    H, W = [int(i) for i in input().split()]
    if H == W == 0:
        break
    for h in range(H):
        for w in range(W):
            if (h+w) % 2 == 0:
                print('#', end='')
            if (h+w) % 2 == 1:
                print('.', end='')

        print()
    print()