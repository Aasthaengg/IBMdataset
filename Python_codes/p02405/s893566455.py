def drawline(odd, columns):
    if odd == 0:
        f = '#'
        s = '.'
    else:
        f = '.'
        s = '#'
    for c in range(columns):
        if c%2 == 0:
            print(f, end='')
        else:
            print(s, end='')
    print('')

while(True):
    H, W = map(int, input().split())
    if W == 0 and H ==0:
        break
    for h in range(H):
        drawline(h%2, W)
    print('')