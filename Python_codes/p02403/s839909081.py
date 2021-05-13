while True:
    H, W = map(int, input().split())
    if (H == W == 0):
        break
    else:
        for j in range(H):
            for i in range(W):
                print("#", end='')
            print()
        print()