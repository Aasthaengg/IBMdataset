import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    H, W = map(int, readline().split())
    S = list(readline().decode('utf-8').strip() for _ in range(H))
    dp = [[INF] * (W) for _ in range(H)]
    if S[0][0]=='#':
        dp[0][0]=1
    else:
        dp[0][0]=0
    for i in range(H):
        for j in range(W):
            if i==H-1 and j == W-1:
                break
            if j==W-1:
                if S[i][j]=='.' and S[i+1][j]=='#':
                    dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1)
                else:
                    dp[i+1][j] = min(dp[i+1][j],dp[i][j])
            elif i == H-1:
                if S[i][j]=='.' and S[i][j+1]=='#':
                    dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
                else:
                    dp[i][j+1] = min(dp[i][j+1],dp[i][j])
            else:
                if S[i][j]=='.' and S[i+1][j]=='#':
                    dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1)
                else:
                    dp[i+1][j] = min(dp[i+1][j],dp[i][j])
                if S[i][j]=='.' and S[i][j+1]=='#':
                    dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
                else:
                    dp[i][j+1] = min(dp[i][j+1],dp[i][j])


    print(dp[H-1][W-1])

if __name__ == '__main__':
    main()