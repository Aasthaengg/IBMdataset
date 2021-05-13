def main():
    h, n = map(int, input().split())
    INF = 10 ** 9
    dp = [INF for _ in range(2*10**4)]
    AB = [tuple(map(int, input().split())) for _ in range(n)]
    dp[0] = 0
    for a, b in AB:
        for i in range(h):
            dp[i + a] = min(dp[i + a], dp[i] + b)
    print(min(dp[h:]))
if __name__ == "__main__":
    main()