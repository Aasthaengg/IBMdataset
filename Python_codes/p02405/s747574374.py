while True:
    [H,W] = raw_input().split()
    H = int(H)
    W = int(W)
    if H == 0 and W == 0:
        break

    for y in range(0,H):
        s = ''
        for x in range(0,W):
            k = x + y
            if k % 2 == 0:
                c = '#'
            else:
                c = '.'
            s = s + c
        
        print s
    print ''