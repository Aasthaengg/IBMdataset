import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    v = list(map(int, readline().split()))
    v.sort()
    cur = v[0]

    for i in range(1, N):
        cur += v[i]
        cur /= 2

    print(cur)


if __name__ == '__main__':
    main()
