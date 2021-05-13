def main():
    s = input()
    op = ["-", "+"]

    for i in range(2 ** 3):
        lst = [0] * 3
        for j in range(3):
            if (i >> j) & 1 == 1:
                lst[2 - j] = 1

        res = int(s[0])
        for j in range(3):
            if lst[j] == 0:
                res -= int(s[j + 1])
            if lst[j] == 1:
                res += int(s[j + 1])
        if res == 7:
            print(f"{s[0]}{op[lst[0]]}{s[1]}{op[lst[1]]}{s[2]}{op[lst[2]]}{s[3]}=7")
            break


if __name__ == "__main__":
    main()
