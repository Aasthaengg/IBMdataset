while True:
    H,W = [int(x) for x in input().split()]
    if (H,W)==(0,0): break
    for i in range(H):
        for j in range(W):
            print("#",end="")
        print("")
    print("")