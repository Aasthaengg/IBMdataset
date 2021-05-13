import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, read().split())

    ans = 1
    for _ in range(N):
        if K < ans:
            ans += K
        else:
            ans *= 2

    print(ans)
    return


if __name__ == '__main__':
    main()
