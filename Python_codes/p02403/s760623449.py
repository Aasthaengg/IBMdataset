while True:
    H,W = map(int,raw_input().split())
    if (H,W) == (0,0):
        break
    for k in range(H):
        print "#"*W
    print ""