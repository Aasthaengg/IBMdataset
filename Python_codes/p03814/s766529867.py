# vim: fileencoding=utf-8


def main():
    s = input()
    i = s.find("A")
    j = s.rfind("Z")
    print(j - i + 1)


if __name__ == "__main__":
    main()
