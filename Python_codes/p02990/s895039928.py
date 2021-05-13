def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = [0] * (k + 1)
    x = n - k + 1
    ans[1] = x
    a, b = n - k, k - 1
    for i in range(2, k + 1):
        x, _ = divmod(x * a * b, i * (i - 1))
        ans[i] = x % mod
        a -= 1
        b -= 1

    print('\n'.join(map(str, ans[1:])))


if __name__ == '__main__':
    main()
