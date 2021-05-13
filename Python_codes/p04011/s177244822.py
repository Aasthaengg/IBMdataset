import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, X, Y = map(int, read().split())

    if N <= K:
        ans = X * N
    else:
        ans = X * K + (N - K) * Y

    print(ans)

    return


if __name__ == '__main__':
    main()
