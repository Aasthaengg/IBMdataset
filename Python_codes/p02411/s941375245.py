while True:
    try:
        m, f, r = map(int, input().split())
        result = ""
        if m == f == r == -1:
            break
        s = m + f
        if m == -1 or f == -1:
            result = "F"
        elif s >= 80:
            result = "A"
        elif s >= 65:
            result = "B"
        elif s >= 50:
            result = "C"
        elif s >= 30:
            if r >= 50:
                result = "C"
            else:
                result = "D"
        elif s >= 0:
            result = "F"
    except EOFError:
        break
    print(result)