def main():
    i = int(input())
    if i == 0:
        print(0)
        exit()

    ans = ""
    while i:
        p, q = divmod(i, 2)
        if q:
            ans += "1"
        else:
            ans += "0"
        i = -p

    print(ans[::-1])


if __name__ == '__main__':
    main()
