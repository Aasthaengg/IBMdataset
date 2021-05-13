import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B = map(int, readline().split())
    A, B = min(A, B), max(A, B)

    if (B - A) % 2 == 1:
        print("IMPOSSIBLE")
    else:
        print((A + B) // 2)


if __name__ == '__main__':
    main()
