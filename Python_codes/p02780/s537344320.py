import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, K = map(int, readline().split())
    P = [0] + list(map(int, readline().split()))

    cur = sum(P[:K])
    s_max = 0

    for i in range(N - K + 1):
        cur += P[K + i]
        cur -= P[i]
        s_max = max(s_max, cur)

    print((s_max + K) / 2)


if __name__ == '__main__':
    main()
