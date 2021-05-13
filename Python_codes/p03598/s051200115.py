import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    K = int(readline())
    x = list(map(int, readline().split()))

    ans = 0

    for i in range(N):
        ans += 2 * min(abs(x[i]), K - x[i])

    print(ans)


if __name__ == '__main__':
    main()
