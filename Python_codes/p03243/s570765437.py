import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    for i in range(N, 1000):
        if len(set(str(i))) == 1:
            return print(i)


if __name__ == '__main__':
    main()
