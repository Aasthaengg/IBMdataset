while 1:
    H, W = map(int, raw_input().split())
    if H == 0 and W == 0:
        break
    else:
        for j in xrange(H):
            print "#" * W
        print ""