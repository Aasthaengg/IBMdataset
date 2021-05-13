import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)

    ans = (p[0] // 2 + sum(p[1:]))
    print(ans)


if __name__ == '__main__':
    main()
