import sys

input = sys.stdin.readline

P = 10 ** 9 + 7


def main():
    N, M = map(int, input().split())
    A = [0] * M
    for i in range(M):
        A[i] = int(input())

    for i in range(M - 1):
        if A[i] + 1 == A[i + 1]:
            print(0)
            exit()

    broken = [False] * (N + 1)
    for a in A:
        broken[a] = True

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1 if not broken[1] else 0

    for i in range(2, N + 1):
        if broken[i]:
            dp[i] = 0
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % P
    
    ans = dp[N]
    print(ans)


if __name__ == "__main__":
    main()
