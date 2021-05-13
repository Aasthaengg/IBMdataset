# ???????????????????????¢??°
def eval(m, f, r):
    if m == -1 or f == -1:
        return "F"
    elif m + f >= 80:
        return "A"
    elif 65 <= m + f < 80:
        return "B"
    elif 50 <= m + f < 65:
        return "C"
    elif 30 <= m + f < 50:
        if r >= 50:
            return "C"
        else:
            return "D"
    elif m + f < 30:
        return "F"


while 1:
    mfr = input().split()
    m = int(mfr[0])
    f = int(mfr[1])
    r = int(mfr[2])

    if m == -1 and f == -1 and r == -1:
        break
    else:
        print(eval(m, f, r))