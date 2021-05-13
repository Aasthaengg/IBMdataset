def main():
    H, N = map(int, input().split())
    magic = [list(map(int, input().split())) for _ in range((N))]
    dp = [float('inf')] * (H + 1)
    dp[0] = 0
    for h in range(H):
        for dmg, cst in magic:
            next = min(h + dmg, H)
            dp[next] = min(dp[next], dp[h] + cst)
    print(dp[h+1])
main()
