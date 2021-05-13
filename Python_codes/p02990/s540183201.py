def main():
    n, k = map(int, input().split())
    m = 10 ** 9 + 7
    x = n - k + 1
    c = [x]
    a, b = n - k, k - 1

    for i in range(2, k + 1):
        x, _ = divmod(x * a * b, (i * (i - 1)))
        c.append(x % m)
        a -= 1
        b -= 1

    print('\n'.join(map(str, c)))


if __name__ == '__main__':
    main()
