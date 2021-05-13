# vim: fileencoding=utf-8


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    flg = 0
    cursol = 0
    for i in a:
        if cursol == 0:
            cursol = i
            continue
        if flg == 0:
            if i > cursol:
                flg = 1
                cursol = i
            elif i < cursol:
                flg = -1
                cursol = i
        elif flg == 1:
            if i >= cursol:
                cursol = i
            elif i < cursol:
                cursol = i
                flg = 0
                ans += 1
        else:
            if i <= cursol:
                cursol = i
            elif i > cursol:
                cursol = i
                flg = 0
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
