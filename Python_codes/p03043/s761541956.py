def main():
    N, K = map(int, input().split())

    ans = 0
    # i is point
    for i in range(1, N + 1):
        x = 0
        while i * (2 ** x) < K:
            x += 1
        ans += 1 / N * (0.5 ** x)

    print(ans)


if __name__ == '__main__':
    main()
