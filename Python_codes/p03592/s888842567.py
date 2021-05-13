import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m, k = map(int, readline().split())

    for row in range(n + 1):
        for col in range(m + 1):
            count = n * m - (row * col) - ((n - row) * (m - col))
            if count == k:
                return print("Yes")

    print("No")


if __name__ == '__main__':
    main()
