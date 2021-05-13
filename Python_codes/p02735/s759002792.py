def main():

    H, W = map(int, input().split())
    s = []
    for _ in range(H):
        t = list(input())
        s.append(t)

    dp = [[float('inf') for _ in range(W+1)] for _ in range(H+1)]

    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                if s[i][j] == "#":
                    dp[i+1][j+1] = 1
                else:
                    dp[i+1][j+1] = 0
            elif i == 0:
                if s[i][j] == s[i][j-1]:
                    dp[i+1][j+1] = dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j] + (s[i][j] == '#')
            elif j == 0:
                if s[i][j] == s[i-1][j]:
                    dp[i+1][j+1] = dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1] + (s[i][j] == '#')
            else:
                if s[i][j] == s[i][j-1]:
                    dp[i+1][j+1] = dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j] + (s[i][j] == '#')
                if s[i][j] == s[i-1][j]:
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1])
                else:
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1] + (s[i][j] == '#'))
    # print(dp)
    return dp[H][W]



if __name__ == '__main__':
    print(main())