import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, Y = map(int, readline().split())

    Y //= 1000

    x, y, z = -1, -1, -1
    for i in range(N + 1):
        for j in range(N + 1):
            k = N - i - j
            if k >= 0 and 10 * i + 5 * j + k == Y:
                x, y, z = i, j, k
                break

    print(x, y, z)
    return


if __name__ == '__main__':
    main()
