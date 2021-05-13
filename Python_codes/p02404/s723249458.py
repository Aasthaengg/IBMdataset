while True:
    H,W = map(int,raw_input().split())
    if H == 0 and W == 0:
        break
    print "#"*W
    for i in range(2,H):
        print "#"+"."*(W-2)+"#"
    print "#"*W
    print ""