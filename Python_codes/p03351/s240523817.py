import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b, c, d = map(int, readline().split())

    def judge():
        if abs(a - c) <= d:
            return True
        if abs(a - b) <= d:
            if abs(b - c) <= d:
                return True
        return False

    if judge():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
