while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        break
    else:
        for i in range(h):
            for j in range(w):
                if j == 0 or j == w-1:
                    print("#",end="")
                else:
                    if i == 0 or i == h-1:
                        print("#",end="")
                    else:
                        print(".",end="")
            print()
        print()
