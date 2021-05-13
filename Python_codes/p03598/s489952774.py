import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *X = map(int, read().split())

    ans = 0
    for x in X:
        ans += min(abs(x), abs(x - K)) * 2

    print(ans)
    return


if __name__ == '__main__':
    main()
