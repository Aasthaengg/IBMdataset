results = []
while True:
    m, f, r = map(int, input().split())
    result = ""
    if m == f == r == -1:
        break
    elif m == -1 or f == -1:
        result = "F"
    else:
        if 80 <= m + f:
            result = "A"
        elif 65 <= m + f < 80:
            result = "B"
        elif 50 <= m + f < 65:
            result = "C"
        elif 30 <= m + f < 50:
            if 50 <= r:
                result = "C"
            else:
                result = "D"
        else:
            result = "F"
    results.append(result)

for result in results:
    print(result)

