while(True):
    H, W = map(int, input().split())
    if(H == W == 0):
        break
    str = ""
    for i in range(W):
        if(i % 2 == 0):
            str += "#"
        else:
            str += "."
    str2 = ""
    for i in range(W):
        if(i % 2 == 0):
            str2 += "."
        else:
            str2 += "#"
    for i in range(H):
        if(i % 2 == 0):
            print(str)
        else:
            print(str2)
    print()