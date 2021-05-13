while(1):
    h,w = [int(i) for i in input().split()]
    if h == 0 and w == 0:
        break
    print("#"*w)
    for i in range(h-2):
        print("#"+"."*(w-2)+"#")
    print("#"*w)
    print("")
    
