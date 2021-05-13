# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(R, C, K, RCV):
    V = [[0] * C for _ in range(R)]
    for r, c, v in RCV:
        r, c = r - 1, c - 1
        V[r][c] = v
    dp = [[[0] * C for _ in range(R)] for __ in range(4)]
    dp[1][0][0] = V[0][0]
    for i in range(R):
        for j in range(C):
            for k in range(4):
                if j > 0:
                    dp[k][i][j] = max(dp[k][i][j], dp[k][i][j - 1])
                    if k > 0:
                        dp[k][i][j] = max(dp[k][i][j], dp[k - 1][i][j - 1] + V[i][j])
                if i > 0:
                    dp[0][i][j] = max(dp[0][i][j], dp[k][i - 1][j])
                    dp[1][i][j] = max(dp[1][i][j], dp[k][i - 1][j] + V[i][j])
    print(max(dp[k][R - 1][C - 1] for k in range(4)))

if __name__ == '__main__':
    input = sys.stdin.readline
    R, C, K = map(int, input().split())
    RCV = [list(map(int, input().split())) for _ in range(K)]
    main(R, C, K, RCV)
