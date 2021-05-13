import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B, C = map(int, readline().split())

    if A + B >= C:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
