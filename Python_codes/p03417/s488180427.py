def main():
    n, m = map(int, input().split())
    if (n, m) == (1, 1):
        print(1)
        exit()

    if n == 1 or m == 1:
        ans = max(0, max(n, m) - 2)
        print(ans)
        return
    else:
        x = max(0, n - 2)
        y = max(0, m - 2)
        ans = x * y
        print(ans)
        return


if __name__ == '__main__':
    main()
