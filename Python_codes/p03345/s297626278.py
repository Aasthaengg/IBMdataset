import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b, c, k = map(int, readline().split())
    if k % 2 == 0:
        diff = a - b
    else:
        diff = b - a

    if abs(diff) > 10 ** 18:
        print("Unfair")
    else:
        print(diff)


if __name__ == '__main__':
    main()
