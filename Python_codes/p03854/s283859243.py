# vim: fileencoding=utf-8


def main():
    s = input()
    c = ["dreamer", "dream", "erase", "eraser"]
    n = [7, 5, 5, 6]
    while True:
        f = True
        for i in range(4):
            if s[-n[i] :] == c[i]:
                f = False
                s = s[: -n[i]]
                break
        if f:
            if len(s) == 0:
                print("YES")
            else:
                print("NO")
            return


if __name__ == "__main__":
    main()
