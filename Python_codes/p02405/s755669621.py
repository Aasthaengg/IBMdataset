while True:
    (H, W) = [int(x) for x in input().split()]
    if H == W == 0:
        break

    for hc in range(H):
        for wc in range(W):
            if (hc + wc) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()