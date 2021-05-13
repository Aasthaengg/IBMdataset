def main():
    s = input()
    k = int(input())
    ans = 0
    tyou = 500000000000000
    for v in s:
        if v == '1':
            ans += 1
        else:
            ans += tyou ** int(v)
        if ans >= k:
            print(v)
            exit()


if __name__ == '__main__':
    main()