import sys

input = sys.stdin.readline
P = 10 ** 9 + 7


def main():
    N = int(input())
    C = [None] * N
    for i in range(N):
        C[i] = int(input())

    MAX_C = 2 * 10 ** 5
    C = [-1] + C
    D = [-1] * (MAX_C + 1)
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        if C[i + 1] == C[i]:
            dp[i + 1] = dp[i]
        else:
            j = D[C[i + 1]]
            if j != -1:
                dp[i + 1] = dp[i] + dp[j]
            else:
                dp[i + 1] = dp[i]
        dp[i + 1] %= P
        D[C[i + 1]] = i + 1

    ans = dp[N]
    print(ans)


if __name__ == "__main__":
    main()
