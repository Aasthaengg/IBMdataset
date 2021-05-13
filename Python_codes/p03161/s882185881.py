def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [0] * n
    for i in range(1, n):
        j = max(0, i-k)
        dp[i] = min(x + abs(h[i] - y) for x, y in zip(dp[j:i], h[j:i]))

    print(dp[-1])
    return


if __name__ == '__main__':
    main()
