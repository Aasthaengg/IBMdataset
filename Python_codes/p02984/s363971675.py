def main():
    n, *a = map(int, open(0).read().split())
    x = sum(a[::2]) - sum(a[1::2])
    ans = str(x)
    tmp = x
    for i in a[:-1]:
        tmp = 2 * i - tmp
        ans += ' ' + str(tmp)
    print(ans)


if __name__ == '__main__':
    main()
