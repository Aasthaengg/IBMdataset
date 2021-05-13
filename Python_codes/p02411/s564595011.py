while 1:
    m,f,r = map(int,raw_input().split())
    if m == f == r:
        break
    if m == -1:
        s = "F"
    elif f == -1:
        s = "F"
    elif m+f >= 80:
        s = "A"
    elif m+f >= 65:
        s = "B"
    elif m+f >= 50:
        s = "C"
    elif m+f >= 30:
        if r >= 50:
            s = "C"
        else:
            s = "D"
    else:
        s = "F"
    print s