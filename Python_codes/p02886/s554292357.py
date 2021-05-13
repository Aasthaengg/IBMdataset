import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    d = list(map(int, readline().split()))

    ans = 0

    for i in range(N):
        for j in range(i + 1, N):
            ans += d[i] * d[j]
    print(ans)


if __name__ == '__main__':
    main()
