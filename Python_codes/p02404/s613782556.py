while(1):
    H, W = map(int, input().split())
    if H==0 and W==0:
        break
    for h in range(H):
        line = ""
        for w in range(W):
            if (h in range(1,H-1)) and (w in range(1,W-1)):
                line += "."
            else:
                line += "#"
        print(line)
    print("")