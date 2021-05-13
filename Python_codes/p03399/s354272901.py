import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a = int(readline())
    b = int(readline())
    c = int(readline())
    d = int(readline())

    ans = min(a, b) + min(c, d)
    print(ans)


if __name__ == '__main__':
    main()
