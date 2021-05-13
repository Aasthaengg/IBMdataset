import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, readline().split())

    ans = 0
    for i in range(K, N + 2):
        left = i * (i - 1) // 2
        right = i * (2 * N - i + 1) // 2
        ans = (ans + right - left + 1) % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
