while True:
    m,f,r = tuple(int(n) for n in input().split())
    if m == f == r == -1:
        break
    if (m == -1 or f == -1) or m + f < 30:
        print("F")
    elif m + f >= 80:
        print("A")
    elif 65 <= m + f < 80:
        print("B")
    elif 50 <= m + f < 65:
        print("C")
    else:
        if r >= 50:
            print("C")
        else:
            print("D")
