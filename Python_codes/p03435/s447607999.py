# vim: fileencoding=utf-8


def main():
    l = list()
    for i in range(3):
        l.append(list(map(int, input().split())))

    for a1 in range(0, l[0][0] + 1):
        b1 = l[0][0] - a1
        b2 = l[0][1] - a1
        b3 = l[0][2] - a1
        a2 = l[1][0] - b1
        a3 = l[2][0] - b1
        if b1 < 0:
            continue
        if b2 < 0:
            continue
        if b3 < 0:
            continue
        if a2 < 0:
            continue
        if a3 < 0:
            continue
        if (
            l[1][1] == b2 + a2
            and l[1][2] == b3 + a2
            and l[2][1] == b2 + a3
            and l[2][2] == b3 + a3
        ):
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
