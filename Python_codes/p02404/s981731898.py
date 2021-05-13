while True:
    h, w= list(map(int,input().split()))
    if h!=0 or w!=0:
        print("#"*w)
        for i in range(h-2):
            print("#"+"."*(w-2)+"#")
        print("#"*w)
        print()
    else:
        break