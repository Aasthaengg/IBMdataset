def main():
    takahashi_cookie, aoki_cookie, operation = map(int, input().split())
    for i in range(operation):
        if i % 2 == 0:
            if takahashi_cookie % 2:
                takahashi_cookie -= 1
            aoki_cookie += takahashi_cookie // 2
            takahashi_cookie //= 2
        else:
            if aoki_cookie % 2:
                aoki_cookie -= 1
            takahashi_cookie += aoki_cookie // 2
            aoki_cookie //= 2
    print(takahashi_cookie, aoki_cookie)


if __name__ == '__main__':
    main()

