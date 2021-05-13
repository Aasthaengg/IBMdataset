def main():
    s = input()
    alphabet = "".join([chr(i) for i in range(97, 97 + 26)])
    if len(s) < 26:
        for i in alphabet:
            if i not in s:
                print(s + i)
                exit()
    else:
        if s == "zyxwvutsrqponmlkjihgfedcba":
            print(-1)
        else:
            for i in reversed(range(26)):
                for j in reversed(range(i + 1, 26)):
                    if s[i] < s[j]:
                        print(s[:i] + s[j])
                        exit()


if __name__ == '__main__':
    main()
