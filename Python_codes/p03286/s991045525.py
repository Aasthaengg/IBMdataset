def main():
    i = int(input())
    if i == 0:
        print(0)
        exit()

    ans = ""
    while i:
        p = i % 2
        ans += str(p)
        i = - (i // 2)

    print(ans[::-1])


if __name__ == '__main__':
    main()
