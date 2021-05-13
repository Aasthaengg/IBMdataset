while True:
    (H, W) = [int(i) for i in input().split()]
    if H == W == 0:
       break

    for a in range(H):
        for b in range(W):
            print('#', end='')
        print()
    print()