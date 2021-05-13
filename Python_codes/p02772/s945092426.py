import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    A = list(map(int, readline().split()))

    def judge():
        for x in A:
            if x % 2 == 0:
                if (x % 3 != 0) and (x % 5 != 0):
                    return False
        return True

    if judge():
        print("APPROVED")
    else:
        print("DENIED")


if __name__ == '__main__':
    main()
