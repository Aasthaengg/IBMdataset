# vim: fileencoding=utf-8


def main():
    s = input()
    p = 700
    if s[0] == "o":
        p += 100
    if s[1] == "o":
        p += 100
    if s[2] == "o":
        p += 100
    print(p)


if __name__ == "__main__":
    main()
