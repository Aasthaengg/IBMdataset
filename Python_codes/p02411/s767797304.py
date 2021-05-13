while True:
    m, f, r = map(int, raw_input().split())
    if m == -1 and f == -1 and r == -1:
        break
    else:
        result = str()
        if m == -1 or f == -1:
            result = 'F'
        elif m + f >= 80:
            result = 'A'
        elif 65 <= m + f < 80:
            result = 'B'
        elif 50 <= m + f < 65:
            result = 'C'
        elif 30 <= m + f < 50 <= r:
            result = 'C'
        elif 30 <= m + f < 50 and r < 50:
            result = 'D'
        elif m + f < 30:
            result = 'F'
        print(result)