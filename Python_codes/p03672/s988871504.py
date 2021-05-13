def main():
    s = input()
    len_s = len(s)

    for i in range(1, len_s - 1):
        if (len_s - i) % 2 != 0:
            continue
        if s[:(len_s - i) // 2] == s[(len_s - i) // 2: len_s - i]:
            print(len_s - i)
            exit()


if __name__ == "__main__":
    main()
