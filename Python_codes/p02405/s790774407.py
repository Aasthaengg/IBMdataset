while True:
    H, W = [int(x) for x in input().split() if x.isdigit()]
    if H ==0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            if j < W-1 and (i + j) % 2 == 0:
                print("#", end='')
            elif j < W-1 and (i + j) % 2 != 0:
                print(".", end='')
            elif j == W-1 and (i + j) % 2 == 0:
                print("#")
            elif j == W-1 and (i + j) % 2 != 0:
                print(".")
    print("")