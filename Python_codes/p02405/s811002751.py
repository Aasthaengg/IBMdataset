while True:
    H,W = map(int,raw_input().split())
    if (H,W) == (0,0):
        break
    for k in range(H):
        if k%2==0 and W%2==0:
            print "#."*(W/2)
        elif k%2==0 and W%2==1:
            print "#."*(W/2)+"#"
        elif k%2==1 and W%2==0:
            print ".#"*(W/2)
        elif k%2==1 and W%2==1:
            print ".#"*(W/2)+"."
    print ""