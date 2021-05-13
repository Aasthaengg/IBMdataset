while True:
    H, W = [int(x) for x in input().split(" ")]
    if H == W == 0:
        break
    for i in range(H):
        if (i + 1) % 2 == 1:
            print( "#." * (W // 2) + "#" * (W % 2))
        else:
            print(".#" * (W // 2) + "." * (W % 2))
    print("")