def main():
    n = int(input())
    # h, w, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()

    while True:
        s = str(n)
        if s[0] == s[1] and s[1] == s[2]:
            print(int(s))
            exit()
        n += 1


if __name__ == '__main__':
    main()
