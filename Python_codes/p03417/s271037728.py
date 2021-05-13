def main():
    n, m = map(int, input().split())
    if n > m:
        n, m = m, n

    if n == 1:
        if m == 1:
            print(1)
            return
        else:
            print(m - 2)
            return
    elif n == 2:
        print(0)
        return
    else:
        print((n - 2) * (m - 2))
        return


if __name__ == '__main__':
    main()
