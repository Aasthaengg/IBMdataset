while True:
    s = input().split(" ")
    m = int(s[0])
    f = int(s[1])
    r = int(s[2])
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1 or m + f < 30:
        print("F")
    elif m + f >= 80:
        print("A")
    elif m + f >= 65:
        print("B")
    elif m + f >= 50:
        print("C")
    else:
        if r >= 50:
            print("C")
        else:
            print("D")