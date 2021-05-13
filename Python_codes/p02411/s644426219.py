for _ in [None] * 50:
    m, f, r = map(int, input().split())
    result = " "
    if m == f == r == -1:
        break
    if m == -1 or f == -1 or m + f < 30:
        result = "F"
    elif m + f >= 80:
        result = "A"
    elif 80 > m + f >= 65:
        result = "B"
    elif 65 > m + f >= 50:
        result = "C"
    else:
        result = "C" if r >= 50 else "D"
    print(result)

