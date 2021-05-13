m, f, r = map(int, input().split())
while 1:
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1\
    or m + f < 30:
        print("F")
    elif m + f < 50:
        if r >= 50:
            print("C")
        else:
            print("D")
    elif m + f < 65:
        print("C")
    elif m + f < 80:
        print("B")
    else:
        print("A")
    m, f, r = map(int, input().split())