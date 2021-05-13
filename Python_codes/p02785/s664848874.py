import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, K = map(int, readline().split())
    H = list(map(int, readline().split()))
    H.sort()

    if N <= K:
        ans = 0
    else:
        ans = sum(H[:N - K])
    print(ans)


if __name__ == '__main__':
    main()
