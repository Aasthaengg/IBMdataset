while True:
    m, f, r = [int(x) for x in input().split(" ")]
    if m == f == r == -1:
        break

    sum = m + f
    if m == -1 or f == -1:
        res = "F"
    elif sum >= 80:
        res = "A"
    elif 65<= sum < 80:
        res = "B"
    elif 50<= sum < 65:
        res = "C"
    elif 30<= sum < 50:
        res = "D"
    else:
        res = "F"

    if res == "D" and r >= 50: res = "C"

    print(res)