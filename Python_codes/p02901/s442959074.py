import sys

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    A = []
    C = []
    for _ in range(M):
        a, b = [int(x) for x in input().split()]
        A.append(a)
        c = [int(x) for x in input().split()]
        tmp = 0
        for cc in c:
            tmp |= 1 << (cc - 1)

        C.append(tmp)

    dp = [float("inf")] * (2 ** N + 1)

    dp[0] = 0

    for i in range(M):
        for k in range(2 ** N + 1):
            next = C[i] | k
            if next >= (2 ** N + 1):
                continue
            dp[next] = min(dp[next], dp[k] + A[i])

    if dp[2 ** N - 1] == float("inf"):
        print(-1)
    else:
        print(dp[2 ** N - 1])


if __name__ == '__main__':
    main()
