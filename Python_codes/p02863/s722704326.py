def main():
    N, T = (int(i) for i in input().split())
    AB = [[int(i) for i in input().split()] for j in range(N)]
    A = [a[0] for a in AB]
    B = [b[1] for b in AB]
    dp1 = [[0]*(T+1) for i in range(N+2)]
    for i in range(1, N+1):
        for j in range(T):
            dp1[i][j] = max(dp1[i][j], dp1[i-1][j])
            if j + A[i-1] < T:
                dp1[i][j + A[i-1]] = \
                    max(dp1[i][j + A[i-1]], dp1[i-1][j] + B[i-1])

    dp2 = [[0]*(T+1) for i in range(N+2)]
    for i in range(1, N+1)[::-1]:
        for j in range(T):
            dp2[i][j] = max(dp2[i][j], dp2[i+1][j])
            if j + A[i-1] < T:
                dp2[i][j + A[i-1]] = \
                    max(dp2[i][j + A[i-1]], dp2[i+1][j] + B[i-1])

    ans = 0
    for i in range(1, N+1):
        for j in range(T):
            ans = max(ans, dp1[i-1][j] + dp2[i+1][T-1-j] + B[i-1])
    print(ans)


if __name__ == '__main__':
    main()
