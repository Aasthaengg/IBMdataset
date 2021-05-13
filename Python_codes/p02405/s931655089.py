while(True):
    H, W = map(int, raw_input().split())

    # Exceptation
    if H == 0 and W == 0:
        break

    # Output Loop
    for i in range(H):
        s = ""

        # Odd Line
        if i%2 == 1:
            for j in range(W):
                if j%2 == 1:
                    s = s + "#"
                else:
                    s = s + "."
        # Even Line
        if i%2 == 0:
            for j in range(W):
                if j%2 == 1:
                    s = s + "."
                else:
                    s = s + "#"
        # Output
        print s
    print