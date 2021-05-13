import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, D, X, *A = map(int, read().split())

    ans = X
    for a in A:
        ans += (D + a - 1) // a

    print(ans)
    return


if __name__ == '__main__':
    main()
