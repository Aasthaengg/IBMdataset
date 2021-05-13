def main():
    N, W = map(int, input().split())
    dp = {0: 0}
    for i in range(N):
        w, v = map(int, input().split())
        nxt = {}
        for k in dp:
            if k+w <= W:
                nxt[k+w] = max(dp[k] + v, dp[k+w] if k+w in dp else 0)
        dp.update(nxt)
    ans = 0
    for k in dp:
        ans = max(ans, dp[k])
    print(ans)


if __name__ == "__main__":
    main()
