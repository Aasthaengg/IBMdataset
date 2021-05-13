import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    mat = []
    a = []
    b = []

    for _ in range(N):
        x, y = map(int, readline().split())
        a.append(x + y)
        b.append(x - y)

    d1 = max(a) - min(a)
    d2 = max(b) - min(b)

    print(max(d1,d2))


if __name__ == '__main__':
    main()
