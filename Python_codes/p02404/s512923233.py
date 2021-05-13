while True:
    H, W = map(int, raw_input().split())
    if H == 0 and W == 0:
        break
    for i in xrange(H):
        if i == 0 or i == H-1:
            print '#'*W
        elif W > 1:
            print '#' + '.'*(W-2) + '#'
        else:
            print '#'
    print 