while(1):
    h,w = [int(i) for i in input().split()]
    if h == 0 and w == 0:
        break
    for i in range(h):
        if i%2 == 0:
            print("#."*(w//2)+"#"*(w%2))
        else:
            print(".#"*(w//2)+"."*(w%2))
    print("")
    
