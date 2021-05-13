def main():
    n, a, b, *x = map(int, open(0).read().split())
    ans = 0
    for i, j in zip(x, x[1:]):
        if a * (j - i) > b:
            ans += b
        else:
            ans += a * (j - i)

    print(ans)


if __name__ == '__main__':
    main()
