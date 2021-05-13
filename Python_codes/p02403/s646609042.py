while True:
    H,W = [int(i) for i in input().split()]
    if H == 0 and W == 0:
        break
    else:
        for j in list(range(1, H+1, 1)):
            for i in list(range(1, W+1, 1)):
                if i == W:
                    print("#")
                else:
                    print("#", end = "")
        print("")
