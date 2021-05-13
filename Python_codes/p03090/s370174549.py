import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())

    if n % 2 == 0:
        m = n * (n - 1) // 2 - n // 2
        print(m)
        for i in range(1, n + 1):
            k = n - i + 1
            for j in range(i + 1, n + 1):
                if j == i or j == k:
                    continue
                print(i, j)
    else:
        m = n * (n - 1) // 2 - n // 2
        print(m)
        for i in range(1, n + 1):
            k = n - i
            for j in range(i + 1, n + 1):
                if j == i or j == k:
                    continue
                print(i, j)


if __name__ == '__main__':
    main()
