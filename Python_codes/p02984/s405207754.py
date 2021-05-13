def main():
    n, *a = map(int, open(0).read().split())
    x1 = sum(a[::2]) - sum(a[1::2])
    x = [0] * n
    x[0] = x1
    for i, j in enumerate(a[:-1], 1):
        x[i] = 2 * j - x[i - 1]
    ans = ' '.join(map(str, x))
    print(ans)


if __name__ == '__main__':
    main()
