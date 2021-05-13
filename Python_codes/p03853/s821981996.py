import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    H, W = map(int, readline().split())

    res = []

    for _ in range(H):
        c = input()
        res.append(c)
        res.append(c)

    for row in res:
        print(row)


if __name__ == '__main__':
    main()
