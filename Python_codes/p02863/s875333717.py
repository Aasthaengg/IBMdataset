import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N, T = map(int, input().split())
    AB = sorted([list(map(int, input().split())) for _ in range(N)])
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    for i in range(N):
        A[i + 1], B[i + 1] = AB[i]

    a_max = max(A)
    t_max = T - 1 + a_max
    dp = [[0 for _ in range(t_max + 1)] for _ in range(N + 1)]

    for i in range(N):
        for j in range(t_max + 1):
            if 0 <= (j - A[i + 1]) and (j - A[i + 1]) < T:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j], dp[i][j - A[i + 1]] + B[i + 1])
            else:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

    ans = 0
    for d in dp:
        ans = max(ans, max(d))

    print(ans)

    # for i in range(t_max + 1):
    #     print("{:03},".format(i), end='')
    # print('')
    # for d in dp:
    #     for a in d:
    #         print("{:03},".format(a), end='')
    #     print('')


if __name__ == '__main__':
    solve()
