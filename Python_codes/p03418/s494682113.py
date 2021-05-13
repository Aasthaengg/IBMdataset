import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, readline().split())

    if K == 0:
        ans = N * N
    else:
        ans = 0
        for b in range(K + 1, N + 1):
            ans += N // b * (b - K) + max(N % b - K + 1, 0)

    print(ans)
    return


if __name__ == '__main__':
    main()
