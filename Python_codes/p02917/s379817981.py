import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *B = map(int, read().split())

    ans = B[0] + B[N - 2]
    for i in range(1, N - 1):
        ans += min(B[i - 1], B[i])

    print(ans)
    return


if __name__ == '__main__':
    main()
