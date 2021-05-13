INF = 10**9 + 7


def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M = (int(i) for i in input().split())
    A = []
    B = []
    C = []
    for _ in range(M):
        a, b = (int(i) for i in input().split())
        A.append(a)
        B.append(b)
        bit = 0
        for s in input().split():
            c = int(s)
            bit |= (1 << (c-1))
        C.append(bit)

    dp = [[INF]*(1 << N) for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(M):
        for j in range(1 << N):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if dp[i][j] != INF:
                next_bit = j | C[i]
                dp[i][next_bit] = min(dp[i][next_bit], dp[i][j] + A[i])
    ans = dp[M][(1 << N) - 1]
    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
