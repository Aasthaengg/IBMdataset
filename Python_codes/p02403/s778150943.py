while 1:
    H,W=[int(i) for i in input().split()]
    if H==W==0:
        break
    else:
        for i in range(H):
            for s in range (W):
                print("#",end="")
            print('')
        print('')