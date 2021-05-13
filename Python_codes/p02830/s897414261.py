import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    S, T = input().split()

    res = ""

    for a, b in zip(S, T):
        res += a
        res += b

    print(res)


if __name__ == '__main__':
    main()
