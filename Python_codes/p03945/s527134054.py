def main():
    s = input()
    before = s[0]
    change = 0
    for i in range(1, len(s)):
        if s[i] != before:
            before = s[i]
            change += 1
    print(change)


if __name__ == '__main__':
    main()

