m, f, r = map(int, input().split())
while not (m == -1 and f == -1 and r == -1):
    if m == -1 or f == -1:
        g = "F"
    elif m + f >= 80:
        g = "A"
    elif m + f >= 65:
        g = "B"
    elif m + f >= 50:
        g = "C"
    elif m + f >= 30:
        if r >= 50:
            g = "C"
        else:
            g = "D"
    else:
        g = "F";
    print(g)
    m, f, r = map(int, input().split())
