import sys
sys.setrecursionlimit(1000000) # 再帰上限を増やす

def main():
    input = sys.stdin.readline  # 文字列に対してinputした場合は、rstripするのを忘れずに！
    N = int(input())
    probability = list(map(float, input().rstrip().split()))

    # dp[i][j] = i枚目までで表がj枚出る確率
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i, p in enumerate(probability, 1):
        for j in range(i+1):
            if j != 0:
                # 表のパターンと裏のパターンの合計
                dp[i][j] = dp[i-1][j] * (1-p) + dp[i-1][j-1] * p
            else:
                # 裏のパターンのみ
                dp[i][j] = dp[i-1][j] * (1-p)
    print(sum(dp[N][(N+1)//2:]))

if __name__ == '__main__':
    main()