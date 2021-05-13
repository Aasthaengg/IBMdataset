import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, K = map(int, readline().split())
    h = list(map(int, readline().split()))
    ans = 0
    for x in h:
        if x >= K:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
