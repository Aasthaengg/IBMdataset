import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = list(map(int, readline().split()))

    for i in range(m // n, 0, -1):
        rem = m - i * n
        if rem % i == 0:
            print(i)
            break


if __name__ == '__main__':
    main()
