while True:
    x = map(int,raw_input().split())
    H = x[0]
    W = x[1]
    if H == 0 and W == 0:
        break
    for i in range(0,H):
        print "#"*W
    print ""