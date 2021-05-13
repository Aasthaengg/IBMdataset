def main():
    S = input()
    cnt = 0
    before, current = '', ''
    for i, c in enumerate(S):
        current += c
        if current != before:
            before = current
            current = ''
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()