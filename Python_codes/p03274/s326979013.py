import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *X = map(int, read().split())

    A = [abs(x - X[0]) for x in X]

    ans = INF
    for i in range(N - K + 1):
        if ans > min(abs(X[i]), abs(X[i + K - 1])) + A[i + K - 1] - A[i]:
            ans = min(abs(X[i]), abs(X[i + K - 1])) + A[i + K - 1] - A[i]

    print(ans)
    return


if __name__ == '__main__':
    main()
