import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    N, Ma, Mb = map(int, input().split())
    A, B, C = [0] * N, [0] * N, [0] * N
    for i in range(N):
        A[i], B[i], C[i] = map(int, input().split())

    INF = 10**10  # INF+INFを計算してもオーバーフローしない範囲で大きく
    I, J, K = N, sum(A), sum(B)
    dp = [[[INF]*(K+1) for _ in range(J+1)] for _ in range(I+1)]
    dp[0][0][0] = 0
    for i in range(1, I+1):
        for j in range(J+1):
            for k in range(K+1):
                # i-1番目を選ぶ場合
                if j >= A[i-1] and k >= B[i-1]:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1]
                                      [j-A[i-1]][k-B[i-1]]+C[i-1])
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
    ans = INF
    for j in range(1,J+1):
        for k in range(1,K+1):
            if k*Ma == j*Mb and k*Ma!=0 and j*Mb!=0:
                ans = min(ans, dp[I][j][k])

    print(-1 if ans == INF else ans)


resolve()