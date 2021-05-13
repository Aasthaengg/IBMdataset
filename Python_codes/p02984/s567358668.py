import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())
    X = [0] * N
    X[-1] = A[-1]
    for i, a in enumerate(A[:-1]):
        if i % 2:
            X[-1] += a
        else:
            X[-1] -= a

    for i in range(N - 2, -1, -1):
        X[i] = 2 * A[i] - X[i + 1]

    print(*X)
    return


if __name__ == '__main__':
    main()
