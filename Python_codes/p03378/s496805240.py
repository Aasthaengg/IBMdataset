import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, M, X = map(int, readline().split())
    A = list(map(int, readline().split()))

    a = 0
    b = 0

    for x in A:
        if x <= X:
            a += 1
        if X <= x:
            b += 1

    print(min(a, b))


if __name__ == '__main__':
    main()
