
def resolve():
    INF = 1<<60
    H, N = map(int, input().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[INF]*(H+1) for _ in range(N+1)]
    for i in range(N):
        dp[i][0] = 0
    
    for i in range(N):
        for j in range(H+1):
            if j < A[i]:
                # 体力がマイナスなっても魔法は使用できる
                dp[i + 1][j] = min(dp[i][j], B[i])
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - A[i]] + B[i])

    print(dp[N][H])


if __name__ == "__main__":
    resolve()
