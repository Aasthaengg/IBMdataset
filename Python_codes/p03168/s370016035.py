from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def read():
    N = int(input().strip())
    P = list(map(float, input().strip().split()))
    return N, P


def solve(N, P):
    # dp[i, j]: i枚目まで投げて、表がj枚出る確率
    # dp[i, j] = dp[i-1, j-1] * p[j] + dp[i, j-1] * (1-p[j])
    # 2000x(N//2)のテーブルを作るとTLEするので、圧縮して解く
    dp = [[0 for j in range(N+1)] for i in range(2)]
    dp[0][0] = 1
    for j in range(1, N+1):
        dp[0][j] = dp[0][j-1] * (1.0 - P[j-1])
    ans = dp[0][-1]
    for i in range(1, N//2+1):
        b = i % 2
        dp[b][i-1] = 0.0
        for j in range(i, N+1):
            dp[b][j] = dp[(b-1)%2][j-1] * P[j-1] + dp[b][j-1] * (1.0 - P[j-1])
        ans += dp[b][-1]
    return "{:.10f}".format(1.0 - ans)


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
