import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x, a, b = map(int, readline().split())

    if abs(x - a) < abs(x - b):
        print("A")
    else:
        print("B")


if __name__ == '__main__':
    main()
