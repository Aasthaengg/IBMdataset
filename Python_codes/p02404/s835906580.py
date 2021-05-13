while True:
    H, W = map(int, input().split())
    if H ==0 and W == 0:
        break
    for i in range(H):
        a = ""
        for j in range(W):
            if i == 0 or i == (H-1):
                a += "#"
            elif j == 0 or j == (W-1):
                a += "#"
            else:
                a += "." 
        print(a)
    print("")