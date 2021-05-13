import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, K = map(int, readline().split())
    ans = K

    for i in range(N - 1):
        ans *= (K - 1)

    print(ans)


if __name__ == '__main__':
    main()
