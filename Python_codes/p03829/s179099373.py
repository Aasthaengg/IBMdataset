import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, A, B, *X = map(int, read().split())

    ans = 0
    for i in range(N - 1):
        if A * (X[i + 1] - X[i]) < B:
            ans += A * (X[i + 1] - X[i])
        else:
            ans += B

    print(ans)
    return


if __name__ == '__main__':
    main()
