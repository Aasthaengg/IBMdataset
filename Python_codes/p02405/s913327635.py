while(1):
    H, W = map(int, input().split())
    if H==0 and W==0:
        break
    for h in range(H):
        line = ""
        for w in range(W):
            if (h + w) % 2 == 0:
                line += "#"
            else:
                line += "."
        print(line)
    print("")