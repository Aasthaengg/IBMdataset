import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = [int(readline()) for _ in range(n)]

    if all([x % 2 == 0 for x in a]):
        print("second")
    else:
        print("first")


if __name__ == '__main__':
    main()
