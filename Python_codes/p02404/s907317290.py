while True:
    [H,W] = raw_input().split()
    H = int(H)
    W = int(W)
    if H == 0 and W == 0:
        break

    for y in range(0,H):
        s = ''
        for x in range(0,W):
            c = '.'
            if x == 0 or x == W - 1:
                c = '#'
            if y == 0 or y == H - 1:
                c = '#'
            
            s = s + c
        
        print s
    print ''