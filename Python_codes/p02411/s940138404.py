while True:
    m, f, r  = [int(_) for _ in input().split()]
    if m == f == r == -1:
        break

    if m == -1 or f == -1:
        rank = "F"
    elif (m + f) >= 80:
        rank = "A"
    elif 65 <= (m + f) < 80:
        rank = "B"
    elif 50 <= (m + f) < 65:
        rank = "C"
    elif 30 <= (m + f) < 50:
        if r >= 50:
            rank = "C"
        else:
            rank = "D"
    else:
        rank = "F"
    print(rank)
