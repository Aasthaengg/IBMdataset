import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    if A[0] != 0:
        print(-1)
        return

    for i in range(N - 1):
        if A[i] + 1 < A[i + 1]:
            print(-1)
            return

    ans = 0
    i = N - 1
    while i > 0:
        M = A[i]
        ans += M
        while A[i] > A[i - 1] and i - 1 >= 0:
            i -= 1
        i -= 1

    print(ans)


if __name__ == "__main__":
    main()
