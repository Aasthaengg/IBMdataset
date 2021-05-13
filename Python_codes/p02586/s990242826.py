import sys
input = sys.stdin.readline
from collections import defaultdict


def read():
    R, C, K = map(int, input().strip().split())
    # アイテムの価値V[r][c]
    V = [defaultdict(int) for i in range(R+1)]
    for i in range(K):
        r, c, v = map(int, input().strip().split())
        V[r][c] = v
    return R, C, K, V


def solve(R, C, K, V, INF=10**9):
    # dp[c][s]: c列目までにs個のアイテムを拾った時の、価値の最大値
    dp = [[-INF for s in range(4)] for c in range(C+1)]
    # 次の行に移るときに使うキャッシュ
    before = [0 for c in range(C+1)]
    for r in range(1, R+1):
        # s=0, s=1, s>1で処理を分ける
        for c in range(1, C+1):
            dp[c][0] = max(dp[c-1][0], before[c])
            dp[c][1] = max(dp[c-1][1], dp[c-1][0] + V[r][c], before[c] + V[r][c])
            for s in range(2, 4):
                dp[c][s] = max(dp[c-1][s], dp[c-1][s-1] + V[r][c])
        # 次の行へ移る
        for c in range(1, C+1):
            before[c] = max(dp[c])
        # dpを初期化
        for c in range(C+1):  
            for s in range(4):
                dp[c][s] = 0
    ans = before[-1]
    return ans


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
