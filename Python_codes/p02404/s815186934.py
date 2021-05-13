while(True):
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    fr = ''
    for i in range(W):
        fr += '#'
    fr += '\n'
    for i in range(H-2):
        fr += '#'
        for j in range(W-2):
            fr += '.'
        fr += '#\n'
    for i in range(W):
        fr += '#'
    fr += '\n'
    print(fr)