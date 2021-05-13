# vim: fileencoding=utf-8


def main():
    s = input()
    li = [0] * 26
    for i in list(s):
        n = ord(i) - ord("a")
        li[n] = 1
    for i in range(26):
        if li[i] == 0:
            print(chr(i + ord("a")))
            return

    print("None")


if __name__ == "__main__":
    main()
