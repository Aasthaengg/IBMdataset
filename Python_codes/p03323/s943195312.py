import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B = map(int, readline().split())

    if A <= 8 and B <= 8:
        print("Yay!")
    else:
        print(":(")


if __name__ == '__main__':
    main()
