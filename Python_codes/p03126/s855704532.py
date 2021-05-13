import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, M = map(int, readline().split())
    cnt = [0] * (M + 1)

    for _ in range(N):
        K, *A = list(map(int, readline().split()))
        for x in A:
            cnt[x] += 1

    print(cnt.count(N))


if __name__ == '__main__':
    main()
