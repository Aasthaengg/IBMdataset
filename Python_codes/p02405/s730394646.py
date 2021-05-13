while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        break
    for x in range(h):
        if x % 2 == 0:
            for y in range(w):
                if y % 2 ==0:
                    print("#",end="")
                else:
                    print(".",end="")
        else:
            for y in range(w):
                if y % 2 == 0:
                    print(".",end="")
                else:
                    print("#",end="")
        print()
    print()
