while True:
    h,w=map(int,input().split())
    if h==0 and w==0:
        break
    for y in range(h):
        for x in range(w):
            print("#",end='')
        print()
    print()