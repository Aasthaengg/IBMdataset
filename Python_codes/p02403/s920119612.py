while(True):
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    line = ''
    for i in range(W):
        line += '#'
    for i in range(H):
        print(line)
    print()