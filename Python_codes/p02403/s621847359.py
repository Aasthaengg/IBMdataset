while True:
    H, W = list(map(int, input().split()))
    if H == 0 and W == 0:
        break
    for height in range(H):
        for wide in range(W):
            print('#', end='')
        print('')
    print('')