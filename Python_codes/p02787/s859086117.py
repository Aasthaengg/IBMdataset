def resolve():
    H, N = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for i in range(N)]
    maxa = max([ab[0] for ab in AB])
    dp = [-1 for _ in range(H+maxa+1)]
    dp[0] = 0
    for i in range(H+1):
        if dp[i] == -1:
            continue
        for a, b in AB:
            dp[i+a] = min(dp[i+a], dp[i]+b) if dp[i+a] != -1 else dp[i]+b
    print(min(filter(lambda x: x != -1, dp[H:])))

    
    
if __name__ == "__main__":
    resolve()
