while True:
    [H,W] = raw_input().split()
    H = int(H)
    W = int(W)
    if H == 0 and W == 0:
        break
        
    for y in range(0,H):
        s = ''
        for x in range(0,W):
            s = s + '#'
        print s
    print ''