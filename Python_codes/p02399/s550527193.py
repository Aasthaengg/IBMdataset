while True:
    a, b = map(int, input().split())
    if a <= 0 or b <= 0:
        break
    elif a > 10 **9 or b > 10**9:
        break
    else:
        d = int(a/b)
        r = int(a%b)
        f = float(a/b)
        print(d, r, "{0:01.5f}".format(f))
        break