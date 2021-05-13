from sys import stdin


def main():
    n = int(stdin.readline())
    ar = map(int, stdin.readline().split())

    f = 0
    s = 0

    cf = 0
    cs = 0

    for idx, val in enumerate(ar):
        cf += val
        cs += val
        if idx % 2 == 0:
            if cf <= 0:
                f += 1 - cf
                cf = 1
            if cs >= 0:
                s += 1 + cs
                cs = -1
        else:
            if cs <= 0:
                s += 1 - cs
                cs = 1
            if cf >= 0:
                f += 1 + cf
                cf = -1
    print(min(s, f))


if __name__ == "__main__":
    main()
