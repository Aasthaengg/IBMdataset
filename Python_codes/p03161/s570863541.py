def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [0] * n
    for i in range(1, n):
        h = a[i]
        cost = 10**9
        for j in range(max(0, i-k), i):
            if dp[j] + abs(h - a[j]) < cost:
                cost = dp[j] + abs(h - a[j])
        dp[i] = cost

    print(dp[n-1])

main()