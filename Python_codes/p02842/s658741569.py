import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    def solve():
        for i in range(100001):
            cur = i * 108 // 100
            if cur == N:
                return i
        return ":("

    print(solve())


if __name__ == '__main__':
    main()
