import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    for i in range(26):
        for j in range(16):
            if 4 * i + 7 * j == N:
                print('Yes')
                return

    print('No')
    return


if __name__ == '__main__':
    main()
