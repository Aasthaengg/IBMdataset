import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *H = map(int, read().split())

    H.sort()

    ans = INF
    for i in range(N - K + 1):
        if ans > H[i + K - 1] - H[i]:
            ans = H[i + K - 1] - H[i]
    print(ans)
    return


if __name__ == '__main__':
    main()
