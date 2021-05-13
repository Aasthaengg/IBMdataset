while True:
    H, W = map(int, input().split())

    if H == 0 and W == 0:
        break

    for x in range(H):
        for y in range(W):
            if (x + y) % 2 == 0: print('#', end='')
            else: print('.', end='')
        print()
    
    print()
