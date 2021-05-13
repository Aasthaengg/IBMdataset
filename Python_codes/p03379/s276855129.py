import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *X = map(int, read().split())

    X = [(x, i) for i, x in enumerate(X)]

    X.sort()

    ans = [0] * N
    for i, (x, j) in enumerate(X):
        if i < N // 2:
            ans[j] = X[N // 2][0]
        else:
            ans[j] = X[N // 2 - 1][0]

    print(*ans, sep='\n')
    return


if __name__ == '__main__':
    main()
