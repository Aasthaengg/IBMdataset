import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, M = map(int, readline().split())
    res = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, readline().split())
        res[a] += 1
        res[b] += 1

    for i in range(1, N + 1):
        print(res[i])


if __name__ == '__main__':
    main()
