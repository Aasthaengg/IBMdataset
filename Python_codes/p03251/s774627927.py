import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, M, X, Y = map(int, readline().split())
    x = list(map(int, readline().split()))
    y = list(map(int, readline().split()))

    def judge():
        for Z in range(X + 1, Y + 1):
            if all(p < Z for p in x) and all(p >= Z for p in y):
                return True
        return False

    if judge():
        print("No War")
    else:
        print("War")


if __name__ == '__main__':
    main()
