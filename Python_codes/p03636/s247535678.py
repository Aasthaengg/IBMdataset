# vim: fileencoding=utf-8


def main():
    s = input()
    res = s[0]
    res += str(len(s) - 2)
    res += s[-1]
    print(res)


if __name__ == "__main__":
    main()
