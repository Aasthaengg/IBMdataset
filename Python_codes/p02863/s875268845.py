def main():
    N, T = (int(i) for i in input().split())
    AB = [[int(i) for i in input().split()] for j in range(N)]
    A = [a[0] for a in AB]
    B = [b[1] for b in AB]

    dp1 = [[0]*T for _ in range(N)]
    dp2 = [[0]*T for _ in range(N+2)]

    for i in range(N-1):
        for j in range(T):
            dp1[i+1][j] = max(dp1[i+1][j], dp1[i][j])
            if 0 <= j - A[i]:
                dp1[i+1][j] = max(dp1[i+1][j], dp1[i][j - A[i]] + B[i])

    for i in range(2, N+1)[::-1]:
        for j in range(T):
            dp2[i][j] = max(dp2[i][j], dp2[i+1][j])
            if 0 <= j - A[i-1]:
                dp2[i][j] = max(dp2[i][j], dp2[i+1][j - A[i-1]] + B[i-1])

    ans = 0
    for i in range(N):
        for j in range(T-1):
            ans = max(ans, dp1[i][j] + dp2[i+2][T - 1 - j] + B[i])
    print(ans)


if __name__ == '__main__':
    main()
