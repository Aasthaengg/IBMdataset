import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = list(map(int, readline().split()))

    for y in x:
        if x.count(y) == 1:
            print(y)


if __name__ == '__main__':
    main()
