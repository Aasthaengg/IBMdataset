def main():
    n = int(input())
    s = input()

    prev = ''
    c = 0

    for i in s:
        if prev == '':
            if i == 'A':
                prev = 'A'
        elif prev == 'A':
            if i == 'A':
                prev = 'A'
            elif i == 'B':
                prev = 'B'
            else:
                prev = ''
        elif prev == 'B':
            if i == 'A':
                prev = 'A'
            elif i == 'C':
                c += 1
                prev = ''
            else:
                prev = ''

    print(c)


if __name__ == '__main__':
    main()
