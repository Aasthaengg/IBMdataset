def main():
    s = int(input())
    x1, y1 = 0, 0
    x2, y2 = 1, int(1e9)
    x3, y3 = 0, 0

    l, r = 1, int(1e9)
    while True:
        m = int((l + r) / 2)
        y = m * int(1e9) - s
        if y < 0:
            l = m + 1
        elif y > 1e9:
            r = m - 1
        else:
            x3, y3 = m, y
            break
    if s == int(1e18):
        x2, y2 = 0, int(1e9)
        x3, y3 = int(1e9), 0
    print(x1, y1, x2, y2, x3, y3)


main()
