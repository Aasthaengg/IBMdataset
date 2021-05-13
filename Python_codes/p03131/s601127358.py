def main():
    k, a, b = map(int, input().split())
    if (b - a) <= 2:
        ans = k + 1
    else:
        n = (k - (a - 1)) // 2
        ans = n * b - (n - 1) * a + (k - (a - 1)) % 2

    print(ans)


if __name__ == '__main__':
    main()
