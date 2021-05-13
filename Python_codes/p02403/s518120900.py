while True:
    (H, W) = tuple([int(i) for i in input().split(' ')])
    if (H == W == 0):
        break
    for i in range(H):
        print('#' * W)
    print()