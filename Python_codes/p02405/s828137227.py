while True:
    H, W = map(int, raw_input().split())
    if (H+W) == 0:
        break
    cb1 = '#'
    cb2 = '.'
    for w in range(W-1):
        if (w % 2) == 0:
            cb1 += '.'
            cb2 += '#'
        else:
            cb1 += '#'
            cb2 += '.'

    for h in range(H/2):
        print cb1
        print cb2
    if (H % 2) != 0:
        print cb1
    print ""