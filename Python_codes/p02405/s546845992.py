while(True):
    (H,W)=[int(s) for s in input().split()]
    if (H,W) == (0,0):
        break
    for j in range(H):
        for k in range(W):
            if (j+k)%2 == 0:
                print("#",end="")
            else:
                print(".",end="")
        print("")
    print("")