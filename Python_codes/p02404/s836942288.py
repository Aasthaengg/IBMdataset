while(True):
    (H,W)=[int(s) for s in input().split()]
    if (H,W) == (0,0):
        break
    print("#"*W)
    for j in range(H-2):
        print("#",end="")
        print("."*(W-2),end="")
        print("#")
    print("#"*W)
    print("")