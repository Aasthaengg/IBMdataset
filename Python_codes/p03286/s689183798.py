def mainusbin(num):
    base = -2
    dst = ""
    i = 0
    if abs(base) > abs(num):
        return num
    while abs(base**i) <= abs(num):
        i += 1
        amari = num % base**i
        if amari:
            dst = "1" + dst
            num -= base**(i-1)
        else:
            dst = "0" + dst
    return dst
src = int(input())
dst = mainusbin(src)
print(dst)
