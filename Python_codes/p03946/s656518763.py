import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A_ = sorted(A)

    j = -1
    diff = 0
    cnt = 0
    MAX = [0] * N
    MAX[-1] = A[-1]
    for i in range(N - 1)[::-1]:
        if A[i] > MAX[i + 1]:
            MAX[i] = A[i]
        else:
            MAX[i] = MAX[i + 1]

    diff = 0
    cnt = 0
    for i in range(N):
        if MAX[i] - A[i] > diff:
            diff = MAX[i] - A[i]
            cnt = 1
        elif MAX[i] - A[i] == diff:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
