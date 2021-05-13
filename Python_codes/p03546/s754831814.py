import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    H, W = map(int, input().split())
    C = []
    for _ in range(10):
        c = list(map(int, input().split()))
        C.append(c)

    A = []
    for _ in range(H):
        a = list(map(int, input().split()))
        A.append(a)

    dp = [[INF] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            dp[i][j] = C[i][j]

    for k in range(10):
        for i in range(10):
            for j in range(10):
                tmp = dp[i][k] + dp[k][j]
                if tmp < dp[i][j]:
                    dp[i][j] = tmp

    ans = 0
    for h in range(H):
        for w in range(W):
            if A[h][w] == -1:
                continue
            else:
                ans += dp[A[h][w]][1]

    print(ans)


if __name__ == "__main__":
    main()
