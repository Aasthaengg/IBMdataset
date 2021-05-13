while True:
    L = map(int,raw_input().split())
    H = (L[0])
    W = (L[1])
    
    if H == 0 and W == 0:break
    for x in range(0,H):
        if x == 0 or x == H-1: print "#" * W
        else: print "#{}#".format("."*(W-2))
        
    print ""