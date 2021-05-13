while True:
    (H, W) = [int(i) for i in input().split()]

    if H == W == 0:
        break

    print("#" * W)
    for i in range(H - 2):
        print("#", "." * (W - 2), "#", sep='')
    print("#" * W)
    print()