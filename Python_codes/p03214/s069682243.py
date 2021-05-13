import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    a = list(map(int, readline().split()))
    S = sum(a)
    b = list(map(lambda x: abs(S - N * x), a))
    print(b.index(min(b)))


if __name__ == '__main__':
    main()
