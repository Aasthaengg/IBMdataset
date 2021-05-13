import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    A = int(readline())

    x = N % 500

    if x <= A:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
