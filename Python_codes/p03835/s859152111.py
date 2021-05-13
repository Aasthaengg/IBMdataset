# vim: fileencoding=utf-8


def main():
    k, s = map(int, input().split())
    c = 0
    for i in range(k + 1):
        for j in range(k + 1):
            z = s - i - j
            if z >= 0 and z <= k:
                c += 1
    print(c)


if __name__ == "__main__":
    main()
