import sys
def input(): return sys.stdin.readline().strip()


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    """まずは縦に何連続かだけ計測"""
    dp = [[0] * W for _ in range(H)]
    # 0列目
    for j in range(W):
        if S[0][j] != '#':
            dp[0][j] = 1
    # dp-part
    for i in range(1, H):
        for j in range(W):
            if S[i][j] != '#':
                dp[i][j] = dp[i - 1][j] + 1
            else:
                num = dp[i - 1][j]
                for k in range(num):
                    dp[i - 1 - k][j] = num
    # last-line
    for j in range(W):
        num = dp[H - 1][j]
        for k in range(num):
            dp[H - 1 - k][j] = num
    
    """次に横に何連続かを計測"""

    dp2 = [[0] * W for _ in range(H)]
    # 0列目
    for i in range(H):
        if S[i][0] != '#':
            dp2[i][0] = 1
    # dp-part
    for j in range(1, W):
        for i in range(H):
            if S[i][j] != '#':
                dp2[i][j] = dp2[i][j - 1] + 1
            else:
                num = dp2[i][j - 1]
                for k in range(num):
                    dp2[i][j - 1 - k] = num
    # last-line
    for i in range(H):
        num = dp2[i][W - 1]
        for k in range(num):
            dp2[i][W - 1 - k] = num
    
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, dp[i][j] + dp2[i][j] - 1)
    print(ans)



if __name__ == "__main__":
    main()
