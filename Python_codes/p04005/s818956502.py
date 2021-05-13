import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    l = list(map(int, readline().split()))
    l.sort()

    if any([x % 2 == 0 for x in l]):
        print(0)
    else:
        s = l[0] * l[1]
        print(s)


if __name__ == '__main__':
    main()
