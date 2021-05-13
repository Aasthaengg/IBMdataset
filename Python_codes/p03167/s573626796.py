import sys
sys.setrecursionlimit(1000000) # 再帰上限を増やす
mod = 1000000007

def main():
    input = sys.stdin.readline  # 文字列に対してinputした場合は、rstripするのを忘れずに！
    H, W = map(int, input().rstrip().split())
    maps = []
    for _ in range(H):
        line = input().rstrip()
        maps.append(line)

    # dp[i][j] = (i, j)までの経路数
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if (i == 0 and j == 0) or maps[i][j] == "#":
                continue
            tmp = 0
            if i - 1 >= 0 and maps[i-1][j] == ".":
                tmp += dp[i-1][j]
                tmp %= mod
            if j - 1 >= 0 and maps[i][j-1] == ".":
                tmp += dp[i][j-1]
                tmp %= mod
            dp[i][j] = tmp
    print(dp[H-1][W-1])

if __name__ == '__main__':
    main()