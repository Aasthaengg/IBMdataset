while True:
    (H, W) = tuple([int(i) for i in input().split(' ')])
    if (H == W == 0):
        break
    for i in range(H):
        if (i == 0):
            # first element
            print('#' * W)
        elif (i == (H - 1)):
            # last element
            print('#' * W)
        else:
            # middle element
            print('#', end='')
            print('.' * (W - 2), end='')
            print('#')
    print()