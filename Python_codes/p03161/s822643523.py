def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [0] * n
    for i in range(1, n):
        h = a[i]
        dp[i] = min([dp[j] + abs(h - a[j]) for j in range(max(0, i-k), i)])

    print(dp[n-1])

main()