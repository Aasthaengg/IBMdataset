
def resolve():
    N, M, Q = map(int, input().split())
    cum_A = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        l, r = map(int, input().split())
        cum_A[l][r] += 1

    # 二次元累積和
    for i in range(1, N+1):
        for j in range(1, N+1):
            cum_A[i][j] += cum_A[i-1][j] + cum_A[i][j-1] - cum_A[i-1][j-1]

    for _ in range(Q):
        ans = 0
        l, r = map(int, input().split())
        ans = cum_A[r][r] - cum_A[r][l-1] - cum_A[l-1][r] + cum_A[l-1][l-1]

        print(ans)

if __name__ == "__main__":
    resolve()