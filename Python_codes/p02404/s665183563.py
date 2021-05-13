while True:    
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    else:
        print("#"*W)
        while H > 2:
            print("#"+"."*(W-2)+"#")
            H -= 1
        print("#"*W)
        print("")