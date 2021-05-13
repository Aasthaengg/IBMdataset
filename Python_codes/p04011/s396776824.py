import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    K = int(readline())
    X = int(readline())
    Y = int(readline())

    ans = 0
    if N <= K:
        ans = N * X
    else:
        ans = K * X + (N - K) * Y

    print(ans)


if __name__ == '__main__':
    main()
