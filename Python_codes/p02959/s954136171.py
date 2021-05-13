import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *AB = map(int, read().split())
    A = AB[: N + 1]
    B = AB[N + 1 :]

    M = sum(A)

    for i in range(N):
        if A[i] > B[i]:
            A[i] -= B[i]
            B[i] = 0
        else:
            B[i] -= A[i]
            A[i] = 0

        A[i + 1] = max(A[i + 1] - B[i], 0)

    print(M - sum(A))
    return


if __name__ == '__main__':
    main()
