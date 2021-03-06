def main():
    n, k = map(int, input().split())
    if k == 0:
        print(n * n)
        return
    ans = 0
    for i in range(k + 1, n + 1):
        p, q = divmod(n, i)
        ans += p * (i - k) + max(q - k + 1, 0)

    print(ans)


if __name__ == '__main__':
    main()
