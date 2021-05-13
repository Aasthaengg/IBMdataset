def main():
    abck = [int(_x) for _x in input().split()]
    a = abck[0]
    b = abck[1]
    c = abck[2]
    k = abck[3]

    kk = k

    total = 0
    if kk >= a:
        kk = kk - a
        total += a
    else:
        print(kk)
        return

    if kk >= b:
        kk = kk - b
    else:
        print(total)
        return

    total = total - kk
    print(total)


main()
