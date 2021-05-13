import sys

input = sys.stdin.readline


def main():
    N = int(input())
    P = [0] * N
    for i in range(N):
        P[i] = int(input())

    dp = [0] * (N + 1)
    for i in range(N):
        p = P[i]
        dp[p] = dp[p - 1] + 1

    ans = N - max(dp)
    print(ans)


if __name__ == "__main__":
    main()
