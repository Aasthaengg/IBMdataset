def resolve():
    H, W, K = list(map(int, input().split()))
    dp = [[0 for _ in range(W)] for __ in range(H+1)]
    dp[0][0] = 1
    mod = 10**9+7
    for h in range(H):
        for w in range(W):
            downleft = 0
            down = 0
            downright = 0
            for bits in range(1<<W-1):
                invalid = False
                for odr in range(W-2):
                    if (bits & (1<<odr)) and (bits & (1<<(odr+1))):
                        invalid = True
                if invalid:
                    continue
                if w > 0 and (bits & (1<<(w-1))):
                    downleft += 1
                elif w < W-1 and (bits & (1<<w)):
                    downright += 1
                else:
                    down += 1
            if w > 0 and downleft > 0:
                dp[h+1][w-1] += downleft*dp[h][w]
                dp[h+1][w-1] %= mod 
            if w < W-1 and downright > 0:
                dp[h+1][w+1] += downright*dp[h][w]
                dp[h+1][w+1] %= mod
            if down > 0:
                dp[h+1][w] += down*dp[h][w]
                dp[h+1][w] %= mod
    print(dp[H][K-1])


if '__main__' == __name__:
    resolve()