import sys
input = sys.stdin.readline

def main():
    H, W, K = map(int, input().split())
    fib = [1, 1]
    for i in range(W-2):
        fib.append(fib[-2] + fib[-1])
    
    nex = [[0] * W for i in range(W)]
    for i in range(W):
        nex[i][i] = fib[i] * fib[W-1-i]
        if i > 0:
            nex[i][i-1] = fib[i-1] * fib[W-i-1]
        if i < W-1:
            nex[i][i+1] = fib[i] * fib[W-i-2]
    MOD = int(1e9) + 7
    dp = [[0] * W for i in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            dp[i+1][j] += dp[i][j] * nex[j][j]
            dp[i+1][j] %= MOD
            if j > 0:
                dp[i+1][j-1] += dp[i][j] * nex[j][j-1]
                dp[i+1][j-1] %= MOD
            if j < W-1:
                dp[i+1][j+1] += dp[i][j] * nex[j][j+1]
                dp[i+1][j+1] %= MOD
    print(dp[H][K-1])


if __name__ == "__main__":
    main()