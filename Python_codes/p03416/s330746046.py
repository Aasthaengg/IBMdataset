# vim: fileencoding=utf-8


def main():
    a, b = map(int, input().split())
    c = 0
    for i in range(a, b + 1):
        #     s = str(i)
        #     r = "".join(reversed(list(s)))
        #     if s == r:
        #         c += 1
        if (i % 10) == (i // 10000) and (i % 100 // 10) == (i % 10000 // 1000):
            c += 1
    print(c)


if __name__ == "__main__":
    main()
