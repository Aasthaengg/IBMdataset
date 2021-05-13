import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x, y = list(map(int, readline().split()))

    ans = 0
    c = x

    while c <= y:
        ans += 1
        c <<= 1

    print(ans)


if __name__ == '__main__':
    main()
