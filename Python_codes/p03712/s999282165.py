import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    H, W = map(int, readline().split())

    res = ["#" * (W + 2)]

    for _ in range(H):
        res += ["#" + input() + "#"]

    res += ["#" * (W + 2)]

    for row in res:
        print(row)


if __name__ == '__main__':
    main()
