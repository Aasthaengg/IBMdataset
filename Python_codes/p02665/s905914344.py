def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = []
    now = 1
    ans = 0
    for i in range(n+1):
        if a[i] > now:
            print(-1)
            return
        else:
            dp.append(now)
            now -= a[i]
            now *= 2
    now = 0
    for i in range(n, -1, -1):
        now += a[i]
        ans += min(now, dp[i])
    print(ans)


main()
