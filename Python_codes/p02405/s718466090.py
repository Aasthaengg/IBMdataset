while 1:
    x = ""
    H, W = map(int ,raw_input().split())
    if H == 0 and W == 0:
        break
    else:
        for i in range(W):
            if i%2 == 0:
                x += '#'
            else:
                x += '.'
        for i in range(H):
            if i%2 == 0:
                print x
            else:
                if len(x)%2 == 0:
                    print x[1:len(x)+1] + '#'
                else:
                    print x[1:len(x)+1] + '.'
        print ""