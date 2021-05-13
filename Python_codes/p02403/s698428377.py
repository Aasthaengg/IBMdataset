while True:
    H, W = [int(i) for i in input().split()]
    if H == W == 0:
        break

    for h in range(H):
        for w in range(W):
            print('#', end='')

        print()

    print()