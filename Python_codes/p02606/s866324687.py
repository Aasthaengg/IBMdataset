import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    l, r, d = map(int, readline().split())

    ans = 0

    for i in range(l, r + 1):
        if i % d == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
