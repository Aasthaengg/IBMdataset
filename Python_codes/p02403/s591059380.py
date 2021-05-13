while True:    
    (H, W) = [int(i) for i in input().split()]
    if H == 0 and W == 0:
        break
    else:
        while H > 0:
            i = W
            while i > 1:
                print("#",end="")
                i -= 1
            print("#")
            H -= 1
        print("")