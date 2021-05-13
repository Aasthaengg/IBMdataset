import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)
MOD = 998244353


def main():
    N = int(input())
    if N % 2 == 0:
        print(N // 2 - 1)
    else:
        print(N // 2)


if __name__ == "__main__":
    main()
