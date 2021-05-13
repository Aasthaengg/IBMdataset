import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *A = map(int, read().split())

    ans = max(N - sum(A), -1)

    print(ans)

    return


if __name__ == '__main__':
    main()
