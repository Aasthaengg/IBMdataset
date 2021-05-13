while True:
    h, w = map(int, raw_input().split())
    if (h == 0) & (w == 0):
        break
    line0 = ""
    line1 = ""
    for i in range(w):
        if i == 0 or i == w - 1:
            line0 += "#"
        else:
            line0 += "."
        line1 += "#"
    for j in range(h):
        if j == 0 or j == h - 1:
            print line1
        else:
            print line0
    print ""